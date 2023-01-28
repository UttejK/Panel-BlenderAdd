import bpy

class My_PT_Panel(bpy.types.Panel):
    bl_idname = "MyPanel"
    bl_label = "MyPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Utils"

    def draw(self, context):
        # row = self.layout.row()
        col = self.layout.column()
        
        col.operator("object.apply_all_modifiers", text="Apply all modifiers")        
        col.operator("object.delete_all_modifiers", text="Cancel all modifiers")
        col.operator("object.shade_smooth_auto", text="Shade auto smooth")