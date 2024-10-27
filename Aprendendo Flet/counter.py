import flet as ft

def main(page: ft.Page):
    page.title = "Increment Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "light"

    text_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def decrement(e):
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e):
        text_number.value = str(int(text_number.value) + 1)
        page.update()
    
    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=decrement),
             text_number,
             ft.IconButton(ft.icons.ADD, on_click=increment)],
             alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)