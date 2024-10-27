import flet as ft


def main(page: ft.Page):
    page.title="My Store"

    def route_store(e):
        page.go("/store")

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        # home
        page.views.append(
            ft.View(
                route='/home',
                controls=[
                    ft.AppBar(title=ft.Text("Home"), bgcolor="blue"),
                    ft.Text(value="Home", size=30),
                    ft.ElevatedButton(text="Go to Store", on_click= route_store)
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
        page.update()
        print(page.views)

        # store
        if page.route == '/store':
            page.views.append(
            ft.View(
                route='/store',
                controls=[
                    ft.AppBar(title=ft.Text("Store"), bgcolor="blue"),
                    ft.Text(value="Store", size=30),
                    ft.ElevatedButton(text="Go Back", on_click=lambda _: page.go('/home'))
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view= page.views[-1]
        page.go(top_view.route)

    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)