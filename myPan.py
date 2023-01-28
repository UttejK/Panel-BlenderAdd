import bpy

class My_PT_Panel(bpy.types.Panel):
    bl_idname = "MyPanel"
    bl_label = "MyPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Ops"

    def draw(self, context):
        layout = self.layout

        # 2 columns with buttons
        row = layout.row()
        col = row.column()
        col.operator("object.apply_all_mods", text="Apply all modifiers")

        col = row.column()
        col.operator("object.cancel_all_mods", text="Cancel all modifiers")


