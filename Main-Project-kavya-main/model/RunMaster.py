from System.Data.CONSTANTS import *
from System.Node import *

print("running runmaster")
Node(NodeType.Master,MASTERPORT).run()