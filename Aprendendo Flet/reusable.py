import flet as ft

class IncrementCounter(ft.UserControl):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.counter = 0
        self.text_number = ft.Text(value=str(self.counter), size=40)

    def increment(self, e):
        self.counter += 1 
        self.text_number.value = str(self.counter)
        self.update()
    
    def build(self):
        return ft.Row(controls=[ft.ElevatedButton(text=self.text, on_click=self.increment),
                                self.text_number],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        width=300)

def main(page: ft.Page):
    page.title = "Reusable App"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    page.add(IncrementCounter("People"),
             IncrementCounter("Animals"),
             IncrementCounter("Food"))

if __name__ == "__main__":
    ft.app(target=main)