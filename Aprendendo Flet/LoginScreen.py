import flet as ft

def main(page: ft.Page):
    page.title="Login Screen"
    page.theme_mode="light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = True
    
    # activate the signup button
    def activate_button(e):
        sign_up_button.disabled = False
        sign_up_button.update()

    # check if all the fields are filled
    def check_change(e):
        if all([username_field.value, password_field.value, checkbox_terms]):
            activate_button(None)
    
    # clear the main page and print the welcome page
    def welcome_page(e):
        page.clean()
        page.add(
            ft.Row(controls=
                    [ft.Text(value=f"Welcome, {username_field.value}!", size=40, color="black", weight="bold")], 
                    alignment=ft.MainAxisAlignment.CENTER)
        )
        page.update()

    # create all the fields
    username_field = ft.TextField(hint_text="Username", text_align=ft.TextAlign.LEFT, width=200, on_change=check_change)
    password_field = ft.TextField(hint_text="Password", password=True, text_align=ft.TextAlign.LEFT, width=200, on_change=check_change)
    checkbox_terms = ft.Checkbox(label="I Agree to Terms", on_change=check_change, value=False)
    sign_up_button = ft.ElevatedButton(text="Sign Up", width=200, disabled=True, on_click=welcome_page)
    
    col =   ft.Column(
                       controls=[
                            username_field,
                            password_field,
                            checkbox_terms,
                            sign_up_button],
                    )
    row = ft.Row(
                [col],
                alignment=ft.MainAxisAlignment.CENTER
            )

    # render the page signup page
    page.add(row)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)