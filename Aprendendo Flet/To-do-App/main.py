import flet as ft

def main(page: ft.Page):
    page.title="To-Do App"
    page.horizontal_alignment = "center"
    page.window_width = 400
    page.window_height = 800
    page.theme_mode="light"

    def add_task(e):       
        task_column.controls.append(
            ft.Row(
                controls=[
                    ft.Checkbox(label=task_field.value)
                ],
                
            )
        )

        task_field.value = ""
        page.update()
        
        

    title = ft.Text(value='Tasks', font_family="arial", color="black", weight="bold", size=40)
    task_field = ft.TextField(hint_text="Whats needs to be done?", width= 200, )
    add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)
    task_line = ft.Row(
        controls=[
            task_field,
            add_button
        ],
        
    )

    task_column = ft.Column(
        controls=[
            task_line
        ],
            alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        title,
        task_column
    )


if __name__=="__main__":
    ft.app(target=main)