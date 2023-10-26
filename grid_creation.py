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

import bpy, bpy_extras, math

from bpy_extras.object_utils import object_data_add
from mathutils import Vector

class GridCreationOperator(bpy.types.Operator, bpy_extras.object_utils.AddObjectHelper):

    bl_idname = 'wm.texelify_grid_creation_op'
    bl_label = 'Create Grid'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        grid_scale = context.scene.texelify_grid_scale
        grid_multiplier = context.scene.texelify_grid_multiplier
        texel_density =  context.scene.texelify_texel_density
        pixel_grid_rotation = context.scene.texelify_grid_rotation
        pixel_grid_viewport_color = context.scene.texelify_viewport_color

        grid_spacing = grid_scale / texel_density
        grid_size = int(grid_scale / (2 * grid_spacing))

        verts = []
        edges = []

        for x in range(-grid_size, grid_size + 1):
            verts.append(Vector((x * grid_spacing, -grid_size * grid_spacing, 0)))
            verts.append(Vector((x * grid_spacing, grid_size * grid_spacing, 0)))
            edges.append((len(verts) - 2, len(verts) - 1))

        for y in range(-grid_size, grid_size + 1):
            verts.append(Vector((-grid_size * grid_spacing, y * grid_spacing, 0)))
            verts.append(Vector((grid_size * grid_spacing, y * grid_spacing, 0)))
            edges.append((len(verts) - 2, len(verts) - 1))

        for x in range(-grid_size, grid_size):
            for y in range(-grid_size, grid_size):
                verts.append(Vector((x * grid_spacing + grid_spacing / 2, y * grid_spacing + grid_spacing / 2, 0)))

        mesh = bpy.data.meshes.new(name="TexelifyMeshGrid")
        mesh.from_pydata(verts, edges, [])

        group = bpy.data.collections.new("TexelifyCollection")
        context.scene.collection.children.link(group)

        start_position = (grid_scale / 2, grid_scale / 2, 0.0)

        for y in range(grid_multiplier):
            for x in range(grid_multiplier):

                position = (start_position[0] + x, start_position[1] + y, start_position[2])

                grid_object = object_data_add(context, mesh, operator=self)
                grid_object.location = position
                grid_object.scale = (1.0, 1.0, 1.0)

                if pixel_grid_rotation == 'UP':
                    grid_object.rotation_euler.y = math.radians(180)
                elif pixel_grid_rotation == 'DOWN':
                    grid_object.rotation_euler.y = math.radians(-180)
                elif pixel_grid_rotation == 'RIGHT':
                    grid_object.rotation_euler.y = math.radians(90)
                elif pixel_grid_rotation == 'LEFT':
                   grid_object.rotation_euler.y = math.radians(-90)

                grid_object.hide_viewport = False
                grid_object.select_set(True)
                   
                grid_object.color = pixel_grid_viewport_color
                grid_object.update_tag()
                
                group.objects.link(grid_object)
                context.scene.collection.objects.unlink(grid_object)
                
        return {'FINISHED'}

class GridCreationUI(bpy.types.Panel):
    
    bl_label = 'Grid Creation'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS' if bpy.app.version < (2, 80) else 'UI'
    bl_category = 'Animation' if bpy.app.version < (2, 80) else 'Texelify'
    
    @classmethod
    def poll(self, context):
        return True
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text = "Grid Scale")
        layout.prop(context.scene, 'texelify_grid_scale', toggle=True)
        layout.label(text = "Grid Multiplier")
        layout.prop(context.scene, 'texelify_grid_multiplier', toggle=True)
        layout.label(text = "Texel Density")
        layout.prop(context.scene, 'texelify_texel_density', toggle=True)
        layout.label(text = "Grid Rotation (Y-axis)")
        layout.prop(context.scene, 'texelify_grid_rotation', expand=True)
        layout.separator()
        
        row = layout.row()
        row.operator("wm.texelify_grid_creation_op")

def register_grid_creation():
    bpy.utils.register_class(GridCreationUI)
    bpy.utils.register_class(GridCreationOperator)

def unregister_grid_creation():
    bpy.utils.unregister_class(GridCreationUI)
    bpy.utils.unregister_class(GridCreationOperator)