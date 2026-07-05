from .blenderTypes import EReportTag
from .config import g_AddonPrefixMap

import bpy



class ReportPackage:

	def __init__(self, inTag: str, inMessage: str):
		self.Tag = {inTag}
		self.Message = inMessage

	Tag: set[str]
	Message: str

def PackReport(inReportTag: EReportTag, inMessage: str) -> ReportPackage:
	return ReportPackage(inReportTag.value[0], inMessage)



def GetRootPrefix() -> str:
	return g_AddonPrefixMap["Addon"] + "."

def GetAddonOpIDPrefix() -> str:
	return GetRootPrefix() + g_AddonPrefixMap["Operator"]

def GetAddonOpID(inName: str) -> str:
	return g_AddonPrefixMap["Operator"] + inName.lower()

def GetAddonFullOpID(inName: str) -> str:
	return GetAddonOpIDPrefix() + inName.lower()

def CallOperatorFunc(inName: str):
	getattr(getattr(bpy.ops, g_AddonPrefixMap["Addon"]), GetAddonOpID(inName))()