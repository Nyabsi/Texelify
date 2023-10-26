# Copyright 2023 Nyabsi
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

bl_info = {
    "name": "Texelify (Beta)",
    "author": "Nabsi",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "File > Import-Export | View3D > UI > Texelify",
    "description": "Drop-in Grid Add-On for Pixel Density Grids for Blender",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export | Object",
}

if "bpy" in locals():
    import importlib
    if "grid_creation" in locals():
        importlib.reload(grid_creation)
    if "grid_modification" in locals():
        importlib.reload(grid_modification)
    if "grid_settings" in locals():
        importlib.reload(grid_settings)
    if "props" in locals():
        importlib.reload(props)

def register():
    from .grid_modification import register_grid_modification
    register_grid_modification()
    from .grid_creation import register_grid_creation
    register_grid_creation()
    from .grid_settings import register_grid_settings
    register_grid_settings()

    from .props import register_props
    register_props()

def unregister():
    from .grid_modification import unregister_grid_modification
    unregister_grid_modification()
    from .grid_creation import unregister_grid_creation
    unregister_grid_creation()
    from .grid_settings import unregister_grid_settings
    unregister_grid_settings()
    
    from .props import unregister_props
    unregister_props()