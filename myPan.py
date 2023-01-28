import bpy

class My_PT_Panel(bpy.types.Panel):
    bl_idname = "MyPanel"
    bl_label = "MyPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Utils"

    def draw(self, context):
        row = self.layout.row()
        
        row.operator("object.apply_all_modifiers", text="Apply all modifiers")        
        row.operator("object.delete_all_modifiers", text="Cancel all modifiers")