from enum import Enum, auto



class ENodeTreeType(Enum):
    GeometryNodeTree = auto(),
    CompositorNodeTree = auto(),
    ShaderNodeTree = auto(),
    TextureNodeTree = auto(),

class ENodeSocketType(Enum):
    DEFAULT = auto(),
    NodeSocketBool = auto(),
    NodeSocketColor = auto(),
    NodeSocketFloat = auto(),
    NodeSocketTexture = auto(),
    NodeSocketVector = auto(),

class ENodeColorTagType(Enum):
    NONE = auto(), 
    ATTRIBUTE = auto(),
    COLOR = auto(),
    CONVERTER = auto(),
    DISTORT = auto(),
    FILTER = auto(),
    GEOMETRY = auto(),
    INPUT = auto(),
    MATTE = auto(),
    OUTPUT = auto(), 
    SCRIPT = auto(),
    SHADER = auto(),
    TEXTURE = auto(),
    VECTOR = auto(),
    PATTERN = auto(),
    INTERFACE = auto(),
    GROUP = auto(),

class ENodeType(Enum):
    # Input and output node
    NodeGroupInput = auto(),
    NodeGroupOutput = auto(),
    
    # Reroute node
    NodeReroute = auto(),

    # Shader nodes
    ShaderNodeAddShader = auto(),
    ShaderNodeCombineXYZ = auto(),
    ShaderNodeGroup = auto(),
    ShaderNodeMath = auto(),
    ShaderNodeMix = auto(),
    ShaderNodeSeparateXYZ = auto(),
    ShaderNodeVectorMath = auto(),


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