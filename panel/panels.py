from ..config import IsSupported, GetAddonPanelName

import bpy



class View3DPanel:
	bl_space_type = "VIEW_3D"
	bl_category = GetAddonPanelName()
	bl_options = {"DEFAULT_CLOSED"}
	bl_region_type = "UI"
	
	@classmethod
	def poll(cls, context: bpy.types.Context):
		return IsSupported()

'''
from ..language import Text
from ..utils import GetAddonFullOpID

class UTILS_PT_Example(View3DPanel, bpy.types.Panel):
	bl_label = "Example Panel"
	bl_idname = "UTILS_PT_Example"
	bl_order = 0

	def draw(self, context: bpy.types.Context):
		self.layout.operator(GetAddonFullOpID("Example"), text=Text("Example Button"))
'''