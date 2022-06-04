from System.Data.CONSTANTS import CRASHPORT
from System.Node import *

print('in runcrash')
Node(NodeType.Crashing ,CRASHPORT).run()
