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

class GridSettingsOperator(bpy.types.Operator):

    bl_idname = "wm.texelify_apply_wireframe_settings_op"
    bl_label = "Configure Wireframe"

    def execute(self, context):
        context.space_data.shading.type = 'WIREFRAME'
        context.space_data.shading.color_type = 'OBJECT'
        context.view_layer.update()
        return {'FINISHED'}

class GridSettingsUI(bpy.types.Panel):
    
    bl_label = 'Settings'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = 'Animation' if bpy.app.version < (2, 80) else 'Texelify'
    
    @classmethod
    def poll(self, context):
        return True
    
    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene, 'texelify_viewport_color', toggle=True)

        row = layout.row()
        row.operator("wm.texelify_apply_wireframe_settings_op")

def register_grid_settings():
    bpy.utils.register_class(GridSettingsUI)
    bpy.utils.register_class(GridSettingsOperator)

def unregister_grid_settings():
    bpy.utils.unregister_class(GridSettingsUI)
    bpy.utils.unregister_class(GridSettingsOperator)