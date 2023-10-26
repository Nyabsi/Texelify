# Copyright 2023 Nabsi
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import bpy
from bpy.props import *

def register_props():
    
    # Grid Settings
    bpy.types.Scene.texelify_grid_scale = FloatProperty(
        name="Grid Scale",
        description="Allows you to customize the Grid scale.",
        default=1,
        min=1
    )

    bpy.types.Scene.texelify_grid_multiplier = IntProperty(
        name="Grid Multiplier",
        description="Makes the Grid larger, to the power of two.",
        default=1,
        min=1,
    )

    bpy.types.Scene.texelify_texel_density = IntProperty(
        name="Texel Density",
        description="Changes the Texel Density of the Grid",
        default=64,
        min=1,
        max=4096
    )
    
    bpy.types.Scene.texelify_grid_rotation = EnumProperty(
        name="Grid Rotation",
        description="Change the rotation of the Grid",
        items=[
            ("RIGHT", "Right", "Sets the Grid rotation to Right"),
            ("LEFT", "Left", "Sets the Grid rotation to Left"),
            ("UP", "Up", "Sets the Grid rotation to Up"),
            ("DOWN", "Down", "Sets the Grid rotation to Down"),
        ],
        default='UP'
    )
    
    # Misc Settings
    bpy.types.Scene.texelify_viewport_color = FloatVectorProperty(
        name="Viewport Color",
        description="Allows you to change the default Viewport color",
        default=(1.0, 1.0, 1.0, 1.0),
        subtype='COLOR',
        size=4,
        min=0.0
    )

def unregister_props():
    
    props = [
        "texelify_grid_scale",
        "texelify_grid_multiplier",
        "texelify_texel_density",
        "texelify_grid_rotation",
        "texelify_viewport_color"
    ]

    for p in props:
        if p in bpy.types.Scene.bl_rna.properties:
            exec("del bpy.types.Scene." + p)