from . import auto_load

from .language import g_LanguageMap

import bpy



def register():

	auto_load.init()
	auto_load.register()

	bpy.app.translations.register(__name__, g_LanguageMap)

def unregister():

	bpy.app.translations.unregister(__name__)

	auto_load.unregister()