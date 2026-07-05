'''
from ..config import IsSupported
from ..utils import GetAddonFullOpID, CallOperatorFunc

import bpy

class UTILS_OT_Call_Example(bpy.types.Operator):
	bl_label = "Call Example"
	bl_idname = GetAddonFullOpID("Call_Example")
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context: bpy.types.Context):
		return IsSupported()

	def execute(self, context: bpy.types.Context):
		pass

class UTILS_OT_Example(bpy.types.Operator):
	bl_label = "Example Operator"
	bl_idname = GetAddonFullOpID("Example")
	bl_options = {"REGISTER", "UNDO"}

	@classmethod
	def poll(cls, context: bpy.types.Context):
		return IsSupported()

	def execute(self, context: bpy.types.Context):
		CallOperatorFunc("Call_Example")
'''