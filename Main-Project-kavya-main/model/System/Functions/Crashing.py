import cv2

from Mosse_Tracker.TrackerManager import TrackerType
from System.Data.CONSTANTS import Work_Crash_Estimation_Only


class Crashing:

    def __init__(self,vif):
        self.vif = vif


    def crash(self,frames,trackers):
        crash_dimentions = []

        # crash_dimentions.extend(self.predict(frames, trackers))
        for i in range(len(trackers)):
            for j in range(i + 1, len(trackers)):
                if i == j:
                    continue
                tracker_A = trackers[i]
                tracker_B = trackers[j]

                #calculate the distance
                asize = pow(pow(tracker_A.vehicle_height, 2) + pow(tracker_A.vehicle_width, 2), 0.5) * .25
                bsize = pow(pow(tracker_B.vehicle_height, 2) + pow(tracker_B.vehicle_width, 2), 0.5) * .25
                dis = asize + bsize

                # asize = pow(pow(tracker_A.vehicle_height, 2) + pow(tracker_A.vehicle_width, 2), 0.5) * .5
                # bsize = pow(pow(tracker_B.vehicle_height, 2) + pow(tracker_B.vehicle_width, 2), 0.5) * .5
                # dis = min(asize,bsize)
                # print(dis)
                if self.checkDistance(tracker_A, tracker_B, 16,dis) or\
                self.checkDistance( tracker_A, tracker_B,19,dis) or\
                self.checkDistance(tracker_A,tracker_B,22,dis) or\
                self.checkDistance( tracker_A, tracker_B, 25,dis) or\
                self.checkDistance( tracker_A, tracker_B, 28,dis):
                    print("#################collision has occured!")
                    ## uncomment next line to work on crash esitamtion only
                    if Work_Crash_Estimation_Only:
                        self.crashEstimation(crash_dimentions,tracker_A,tracker_B,frames)
                    else:
                        crash_dimentions.extend(self.predict(frames, [tracker_B, tracker_A]))
        if len(crash_dimentions) > 0:
            xmin = 10000
            ymin = 10000
            xmax = 0
            ymax = 0
            for crash_dimension in crash_dimentions:
                xmin = min(xmin, crash_dimension[0])
                ymin = min(ymin, crash_dimension[1])
                xmax = max(xmax, crash_dimension[2])
                ymax = max(ymax, crash_dimension[3])
            crash_dimentions = [xmin,ymin,xmax,ymax]
        else:
            crash_dimentions = []


        return crash_dimentions

    def checkDistance(self, tracker_A, tracker_B, frame_no,dis):
        if not tracker_A.isAboveSpeedLimit(frame_no - 10, frame_no) and not tracker_B.isAboveSpeedLimit(frame_no - 10,frame_no):
            return False

        xa, ya = tracker_A.estimationFutureCenter[frame_no]
        xb, yb = tracker_B.estimationFutureCenter[frame_no]
        r = pow(pow(xa - xb, 2) + pow(ya - yb, 2), 0.5)


        if r == 0:
            return True
        elif r > dis: #40
            # print("distance false")
            return False

        if tracker_A.tracker_type == TrackerType.MOSSE:
            xa_actual, ya_actual = tracker_A.tracker.centers[frame_no]
            xb_actual, yb_actual = tracker_B.tracker.centers[frame_no]
        else:
            xa_actual, ya_actual = tracker_A.get_position(tracker_A.history[frame_no])
            xb_actual, yb_actual = tracker_B.get_position(tracker_B.history[frame_no])
        difference_trackerA_actual_to_estimate = pow(pow(xa_actual - xa, 2) + pow(ya_actual - ya, 2), 0.5)
        difference_trackerB_actual_to_estimate = pow(pow(xb_actual - xb, 2) + pow(yb_actual - yb, 2), 0.5)
        max_difference = max(difference_trackerA_actual_to_estimate, difference_trackerB_actual_to_estimate)


        if max_difference / r > 0.5:
            # print(r,difference_trackerA_actual_to_estimate,difference_trackerB_actual_to_estimate,max_difference/r)
            return True
        return False

    def predict(self,frames_RGB, trackers):
        gray_frames = self.convertToGrayFrames(frames_RGB)
        no_crash = 0
        crash = 0


        crash_dimentions = []
        for tracker in trackers:
            tracker_frames, width, height, xmin, xmax, ymin, ymax = tracker.getFramesOfTracking(gray_frames)
            crash_dimentions.append([xmin,ymin,xmax,ymax])

            if tracker_frames == None:
                continue

            if xmax - xmin < 50:  # 50
                continue
            if ymax - ymin <= 28:  # 35
                continue

            if (ymax - ymin) / (xmax - xmin) < 0.35:  # 0.35
                continue

            feature_vec = self.vif.process(tracker_frames)
            result = self.vif.clf.predict(feature_vec.reshape(1, 304))
            if result[0] == 0.0:
                no_crash += 1
            else:
                crash += 1
                tracker.saveTracking(frames_RGB)



        if crash == 0:
            crash_dimentions = []
        # print(crash, no_crash)
        return crash_dimentions




    def convertToGrayFrames(self,frames_RGB):
        gray_frames = []
        for frame in frames_RGB:
            gray_frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        return gray_frames


    def crashEstimation(self,crash_dimentions,tracker_A,tracker_B,frames):
        tracker_frames, width, height, xmin, xmax, ymin, ymax = tracker_A.getFramesOfTracking(
            self.convertToGrayFrames(frames))
        if xmax - xmin < 50 or ymax - ymin <= 28 or (ymax - ymin) / (xmax - xmin) < 0.35 :  # 50
           pass
        else:
            crash_dimentions.extend([[xmin, ymin, xmax, ymax]])
        tracker_frames, width, height, xmin, xmax, ymin, ymax = tracker_B.getFramesOfTracking(
            self.convertToGrayFrames(frames))

        if xmax - xmin < 50 or ymax - ymin <= 28 or (ymax - ymin) / (xmax - xmin) < 0.35:  # 50
            pass
        else:
            crash_dimentions.extend([[xmin, ymin, xmax, ymax]])
