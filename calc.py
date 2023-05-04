import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)

class CalcApp(UserControl):
    def build(self):
        self.result = Text(value="0", size=30)

        return Container(
            content=Column(
                controls=[
                    Row(controls=[self.result]),
                    Row(controls=[
                        ElevatedButton(text="AC",expand=1,on_click=self.button_click,data="AC"),
                        ElevatedButton(text="+/-",expand=1,on_click=self.button_click,data="+/-"),
                        ElevatedButton(text="%",expand=1,on_click=self.button_click,data="%"),
                        ElevatedButton(text="/",expand=1,on_click=self.button_click,data="/"),
                    ]),
                    Row(controls=[
                        
                    ])
                ]
            )
        )
    
    def button_click(self, e):
        pass
    
def main(page: ft.Page):
    page.title = "Calculator"

    # window size setting
    page.window_width = 300
    page.window_min_width = 300
    page.window_max_width = 300
    page.window_height = 350
    page.window_min_height = 350
    
    calc = CalcApp()
    page.add(calc)
    

ft.app(target=main)