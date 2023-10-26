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

import bpy

# TODO: implement this.
class GridModificationOperator(bpy.types.Operator):
    pass

class GridMofificationUI(bpy.types.Panel):
    
    bl_label = 'Modification'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = 'Animation' if bpy.app.version < (2, 80) else 'Texelify'

    @classmethod
    def poll(self, context):
        return True
    
    def draw(self, context):
        layout = self.layout

        if "TexelifyCollection" in context.collection.name:
            layout.label(text=f"Selected {context.collection.name}")
        else:
            layout.label(text=f"No Grid collection selected")

def register_grid_modification():
    bpy.utils.register_class(GridMofificationUI)

def unregister_grid_modification():
    bpy.utils.register_class(GridMofificationUI)