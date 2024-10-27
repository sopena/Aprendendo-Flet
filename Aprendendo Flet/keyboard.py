import flet as ft

def main(page: ft.Page):
    page.title="Keyboard Pro"
    page.theme_mode = "light"
    page.spacing = 30
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    

    key = ft.Text(value="Key", size=30)
    shift = ft.Text(value="Shift", size=30, color="red")
    ctrl = ft.Text(value="Control", size=30, color="blue")
    alt = ft.Text(value="Alt", size=30, color="green")
    
    def on_keyboard(e):
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        print(e.data)
        page.update()

    page.on_keyboard_event = on_keyboard

    page.add(
        ft.Text("Press any combination of keys..."),
        ft.Row(controls = [key, shift, ctrl, alt],
               alignment = ft.MainAxisAlignment.CENTER),
        
    )

if __name__ == "__main__":
    ft.app(target=main)