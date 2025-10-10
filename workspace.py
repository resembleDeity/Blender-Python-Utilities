import bpy

from .blenderTypes import EWorkspaceType
from .customTypes import ECustomWorkspaceType


def SwitchWorkspace(inWorkspaceType: EWorkspaceType):
    bpy.context.window.workspace = bpy.data.workspaces[inWorkspaceType.value]

def SwitchCustomWorkspace(inWorkspaceType: ECustomWorkspaceType):
    bpy.context.window.workspace = bpy.data.workspaces[inWorkspaceType.value]