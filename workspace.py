from .blenderTypes import EWorkspaceType, EReportTag
from .customTypes import ECustomWorkspaceType
from .language import Text
from .utils import ReportPackage, PackReport

import bpy

from functools import singledispatch



def GetWorkspace() -> bpy.types.WorkSpace:
	'''
	Get current active workspace
	'''
	return bpy.context.window.workspace

def GetWorkspaces() -> bpy.types.BlendDataWorkSpaces:
	'''
	Get current all workspace
	'''
	return bpy.data.workspaces



@singledispatch
def SetWorkspace(inWorkspaceType: str):
	bpy.context.window.workspace = bpy.data.workspaces[inWorkspaceType]

@SetWorkspace.register(EWorkspaceType)
def _(inWorkspaceType: EWorkspaceType):
	SetWorkspace(inWorkspaceType.value)

@SetWorkspace.register(ECustomWorkspaceType)
def _(inWorkspaceType: ECustomWorkspaceType):
	SetWorkspace(inWorkspaceType.value)



@singledispatch
def HasWorkspace(inWorkspaceType: str) -> bool:
	return inWorkspaceType in GetWorkspaces()

@HasWorkspace.register(EWorkspaceType)
def _(inWorkspaceType: EWorkspaceType) -> bool:
	return HasWorkspace(inWorkspaceType.value)

@HasWorkspace.register(ECustomWorkspaceType)
def _(inWorkspaceType: ECustomWorkspaceType) -> bool:
	return HasWorkspace(inWorkspaceType.value)



@singledispatch
def SwitchWorkspace(inWorkspaceType: str) -> ReportPackage:
	translation = Text(inWorkspaceType)
	if HasWorkspace(inWorkspaceType):
		SetWorkspace(inWorkspaceType)
		return PackReport(EReportTag.Info, "Switched workspace successfully.")
	
	if HasWorkspace(translation):
		SetWorkspace(inWorkspaceType)
		return PackReport(EReportTag.Info, "Switched workspace successfully.")
	
	return PackReport(EReportTag.Error, f"Workspace '{inWorkspaceType}' or '{translation}' not found.")

@SwitchWorkspace.register(EWorkspaceType)
def _(inWorkspaceType: EWorkspaceType) -> ReportPackage:
	return SwitchWorkspace(inWorkspaceType.value)

@SwitchWorkspace.register(ECustomWorkspaceType)
def _(inWorkspaceType: ECustomWorkspaceType) -> ReportPackage:
	return SwitchWorkspace(inWorkspaceType.value)