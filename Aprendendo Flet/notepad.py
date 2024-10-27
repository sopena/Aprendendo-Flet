import flet as ft
import os

class TextEditor(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.text_field = ft.TextField(multiline=True,
                                       autofocus=True,
                                       border=ft.InputBorder.NONE,
                                       min_lines=40,
                                       on_change=self.save_text,
                                       content_padding=30,
                                       cursor_color="yellow")
        
        
    
    def save_text(self, e):
        with open('save.txt', 'w') as f:
            f.write(self.text_field.value)
    
    def read_text(self):
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.text_field.hint_text = 'Welcome to the text editor!'
    
    def build(self):
        self.text_field.value = self.read_text()
        return self.text_field


def main(page: ft.Page):
    page.title="Keyboard Pro"
    page.theme_mode = "dark"
    page.spacing = 5
    page.horizontal_alignment = "center"
    page.scroll=True
    
    

    page.add(TextEditor())
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
