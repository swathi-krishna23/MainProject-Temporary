import sys
import os

from project.settings import BASE_DIR
from .System.Data.CONSTANTS import *
# from System.Data.CONSTANTS import *
from .System.CameraNode import CameraNode
import random

cities = ['Cairo', 'Alexandria', 'Gizah', 'Shubra El-Kheima', 'Port Said', 'Suez', 'Luxor', 'Al-Mansura',
         'Tanta', 'Asyut', 'Ismailia', 'Fayyum', 'Zagazig', 'Aswan', 'Damietta',
          'Damanhur', 'Al-Minya', 'Beni Suef', 'Qena', 'Sohag', 'Hurghada', 'Shibin El Kom',
          'Banha', 'Arish', 'Mallawi', 'Bilbais', 'Marsa Matruh',
          'Idfu, Mit Ghamr', 'Al-Hamidiyya', 'Desouk', 'Qalyub', 'Abu Kabir', 'Girga', 'Akhmim', 'Matareya']

def sendToBk(vidpath):
        global cities
        print(vidpath, '**vidpath**')
        video_id = vidpath.split('.')[0]
        video_id = video_id.split('\\')
        video_id = int(video_id[-1][:4])
        print(str(video_id) + " "+" in run camera")
        print("hello"+"run camera")
        CameraNode(video_id, '/media/' + str(video_id) + '.mp4',files=Work_Detect_Files, city= random.choice(cities), district_no= 'District ' + str(random.randint(1, 30))).start()
        # CameraNode(video_id,vidpath,files=Work_Detect_Files, city= random.choice(cities), district_no= 'District ' + str(random.randint(1, 30))).start()
        print(str(BASE_DIR)+ " "+"in run camera")
        print("runcamera done")
        # os.system('python '+str(BASE_DIR)+'model\RunCrash.py')
        os.system('python model/RunMaster.py & python model/RunDetect.py & python model/RunTracker.py & python model/RunCrash.py')
        print("last line of runcamera")