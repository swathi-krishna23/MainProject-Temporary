import multiprocessing

from System.Data.CONSTANTS import *
from System.Node import *

print("in Tracker.py")
Node(NodeType.Tracking, TRACKPORT).run()
