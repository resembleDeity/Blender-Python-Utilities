import bpy



g_LanguageMap: dict[str, dict[tuple[str, str], str]] = {
	"zh_HANS": {
		# Addon
		("*", "Utils"): "工具",

		# Panel
		("*", "Example Panel"): "示例面板",

		# Subpanel

		# Operator
		("Operator", "Example Operator"): "示例操作",

		# Property

	},
	#"en_US": { },
}

g_TextMap: dict[str, dict[str, str]] = {
	"zh_HANS": {
		"Example Button": "示例按钮",
	},
}



def GetLanguageCode() -> str:
	return bpy.context.preferences.view.language

def Text(inText: str) -> str:
	translation = bpy.app.translations.pgettext(inText)
	if inText != translation:
		return translation

	languageCode = GetLanguageCode()
	if languageCode not in g_TextMap:
		return inText
	
	if inText not in g_TextMap[languageCode]:
		return inText
	
	return g_TextMap[languageCode][inText]