from enum import Enum



class ENodeTreeType(Enum):
	GeometryNodeTree = "GeometryNodeTree",
	CompositorNodeTree = "CompositorNodeTree",
	ShaderNodeTree = "ShaderNodeTree",
	TextureNodeTree = "TextureNodeTree",

class ENodeSocketType(Enum):
	DEFAULT = "DEFAULT",
	Bool = "NodeSocketBool",
	Color = "NodeSocketColor",
	Float = "NodeSocketFloat",
	Texture = "NodeSocketTexture",
	NodeSocketVector = "NodeSocketVector",

class ENodeColorTagType(Enum):
	NONE = "NONE", 
	ATTRIBUTE = "ATTRIBUTE",
	COLOR = "COLOR",
	CONVERTER = "CONVERTER",
	DISTORT = "DISTORT",
	FILTER = "FILTER",
	GEOMETRY = "GEOMETRY",
	INPUT = "INPUT",
	MATTE = "MATTE",
	OUTPUT = "OUTPUT", 
	SCRIPT = "SCRIPT",
	SHADER = "SHADER",
	TEXTURE = "TEXTURE",
	VECTOR = "VECTOR",
	PATTERN = "PATTERN",
	INTERFACE = "INTERFACE",
	GROUP = "GROUP",

class ENodeType(Enum):
	# Input and output node
	Input = "NodeGroupInput",
	Output = "NodeGroupOutput",
	
	# Reroute node
	Reroute = "NodeReroute",

	# Shader nodes
	ShaderNodeAddShader = "ShaderNodeAddShader",
	ShaderNodeCombineXYZ = "ShaderNodeCombineXYZ",
	ShaderNodeGroup = "ShaderNodeGroup",
	ShaderNodeMath = "ShaderNodeMath",
	ShaderNodeMix = "ShaderNodeMix",
	ShaderNodeSeparateXYZ = "ShaderNodeSeparateXYZ",
	ShaderNodeVectorMath = "ShaderNodeVectorMath",



class EWorkspaceType(Enum):
	Animation = "Animation"
	Compositing = "Compositing"
	GeometryNodes = "Geometry Nodes"
	Layout = "Layout"
	Modeling = "Modeling"
	Rendering = "Rendering"
	Scripting = "Scripting"
	Sculpting = "Sculpting"
	Shading = "Shading"
	TexturePaint = "Texture Paint"
	UVEditing = "UV Editing"



class EReportTag(Enum):
	Debug = "DEBUG",  # Debug.
	Info = "INFO",  # Info.
	Operator = "OPERATOR",  # Operator.
	Property = "PROPERTY",  # Property.
	Warning = "WARNING",  # Warning.
	Error = "ERROR",  # Error.
	InvalidInput = "ERROR_INVALID_INPUT",  # Invalid Input.
	InvalidContext = "ERROR_INVALID_CONTEXT",  # Invalid Context.
	OutOfMemory = "ERROR_OUT_OF_MEMORY",  # Out of Memory.