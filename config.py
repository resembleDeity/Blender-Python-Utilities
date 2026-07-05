import bpy

import os



g_RootPath = os.path.dirname(__file__)

def JoinPath(inPath: str, inJoin: str) -> str:
	return os.path.join(inPath, inJoin)

def GetRootPath() -> str:
	return g_RootPath

def GetFullPath(inName: str) -> str:
	return JoinPath(GetRootPath(), inName)

# g_AssetsPath = GetFullPath("addons/assets") -> YourAddon/addons/assets/
g_AssetsPath = GetFullPath("assets") # -> YourAddon/assets/

def GetAssetsPath() -> str:
	return g_AssetsPath



type Version = tuple[int, int, int]

def GetBlenderVersion() -> Version:
	return bpy.app.version 

g_MinSupportedVersion: Version = (3, 0, 0)

def GetSupportedMinVersion() -> Version:
	return g_MinSupportedVersion

def IsSupported() -> bool:
	return GetBlenderVersion() >= GetSupportedMinVersion()



g_AddonPanelName = "Utils"

def GetAddonPanelName() -> str:
	return g_AddonPanelName



g_AddonPrefixMap: dict[str, str] = {
	"Addon": "utils",
	"Operator": "op_",
}
'''
Key "Addon" is represents root prefix(usually use Addon name),
but root prefix is a module(Addon) type, so please use `utils.GetRootPrefix()` get prefix as separators.

Other Key please use "_" or other character as separators.

The prefix concatenation rules is "Addon" + "Other" + name.

Please refer to `utils.GetAddonOpIDPrefix()`
'''