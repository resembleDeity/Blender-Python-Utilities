from typing import Literal

import mathutils
import bpy
from bpy.types import NodeTree
from bpy.types import Nodes, Node
from bpy.types import NodeTreeInterface, NodeSocket
from bpy.types import NodeLinks, NodeLink

from .blenderTypes import ENodeTreeType
from .blenderTypes import ENodeType, ENodeSocketType, ENodeColorTagType



class InterfaceSocket:

    def __init__(
        self, 
        inName: str, 
        inInOut: str, 
        inSocketType: ENodeSocketType | None = ENodeSocketType.DEFAULT
    ):
        self.name = inName
        self.inOut = inInOut
        self.socketType = inSocketType

    name: str
    inOut : str
    socketType: ENodeSocketType


def NewLink(
    inLinks: NodeLinks, 
    inInput: NodeSocket, 
    inOutput: NodeSocket
) -> NodeLink:
    return inLinks.new(inInput, inOutput)

def NewNodeGroup(
    inGroupName: str, 
    inNodeTreeType: ENodeTreeType,
    inGroupColor: ENodeColorTagType | None = ENodeColorTagType.GROUP,
) -> NodeTree:
    if inGroupName in bpy.data.node_groups:
        return bpy.data.node_groups[inGroupName]

    nodeGroup = bpy.data.node_groups.new(inGroupName, inNodeTreeType.name)
    nodeGroup.color_tag = inGroupColor.name

    return nodeGroup

def NewNodeSocket(
    inInterface: NodeTreeInterface, 
    inName: str, 
    inInOut: Literal['INPUT', 'OUTPUT'] | None = "INPUT",
    inSocketType: ENodeSocketType | None = ENodeSocketType.DEFAULT
) -> NodeSocket:
    inInterface.new_socket(name=inName, in_out=inInOut, socket_type=inSocketType.name)

def NewNodeSockets(
    inInterface: NodeTreeInterface,
    inSocketList: list[InterfaceSocket]
) -> NodeSocket:
    for socket in inSocketList:
        NewNodeSocket(inInterface, socket.name, socket.inOut, socket.socketType)



def GetNode(
    inNodes: Nodes, 
    inNodeType: ENodeType, 
    inLocation: mathutils.Vector,
) -> Node:
    node = inNodes.new(inNodeType.name)
    node.location = inLocation

    return node

def GetNodeGroupInputAndOutput(inNodes: Nodes):
    return (
        GetNode(inNodes, ENodeType.NodeGroupInput, (-300, 0)),
        GetNode(inNodes, ENodeType.NodeGroupOutput, (300, 0)),
    )

def GetNodeGroup(
    inNodes: Nodes,
    inNodeTree: NodeTree, 
    inNodeType: ENodeType,
    inLocation: mathutils.Vector,
) -> Node:
    node = GetNode(inNodes, inNodeType, inLocation)
    node.node_tree = inNodeTree

    return node