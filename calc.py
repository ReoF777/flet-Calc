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
        self.num = 0
        self.is_new = False
        self.operand_select = False
        self.operand = ""

        return Container(
            width=300,
            height=390,
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
                        ElevatedButton(text="7",expand=1,on_click=self.button_click,data="7"),
                        ElevatedButton(text="8",expand=1,on_click=self.button_click,data="8"),
                        ElevatedButton(text="9",expand=1,on_click=self.button_click,data="9"),
                        ElevatedButton(text="*",expand=1,on_click=self.button_click,data="*"),   
                    ]),
                    Row(controls=[
                        ElevatedButton(text="4",expand=1,on_click=self.button_click,data="4"),
                        ElevatedButton(text="5",expand=1,on_click=self.button_click,data="5"),
                        ElevatedButton(text="6",expand=1,on_click=self.button_click,data="6"),
                        ElevatedButton(text="-",expand=1,on_click=self.button_click,data="-"),
                    ]),
                    Row(controls=[
                        ElevatedButton(text="1",expand=1,on_click=self.button_click,data="1"),
                        ElevatedButton(text="2",expand=1,on_click=self.button_click,data="2"),
                        ElevatedButton(text="3",expand=1,on_click=self.button_click,data="3"),
                        ElevatedButton(text="+",expand=1,on_click=self.button_click,data="+"),
                    ]),
                    Row(controls=[
                        ElevatedButton(text="0",expand=2,on_click=self.button_click,data="0"),
                        ElevatedButton(text=".",expand=1,on_click=self.button_click,data="."),
                        ElevatedButton(text="=",expand=1,on_click=self.button_click,data="="),
                    ]),
                ]
            )
        )
    
    def button_click(self, e):
        data = e.control.data

        if(str.isdigit(data)):
            self.input_num=int(data)
            self.operand_select = False
            self.operand = "Nan"

            if(self.operand_select):
                if(self.operand == "+"):
                    pass
                
            else:
                self.num = self.num *10 + self.input_num

            self.result.value = self.num

        elif(data == "+"):
            self.operand_select = True
            self.operand = "+"

        elif(data == "-"):
            self.operand_select = True
            self.operand = "-"

        elif(data == "*"):
            self.operand_select = True
            self.operand = "*"

        elif(data == "/"):
            self.operand_select = True
            self.operand = "/"

        elif(data == "%"):
            self.operand_select = True
            self.num = self.num / 100

        elif(data == "."):
            pass

        elif(data == "+/-"):
            self.num = self.num * -1

        elif(data == "="):
            self.operand_select = True
            if(self.operand == "Plus"):
                pass
            elif(self.operand == "Minus"):
                pass
            elif(self.operand == "Divide"):
                pass
            else:
                pass

        else:
            self.operand_select = False
            self.result.value = 0
            self.operand = 0

        self.result.value = self.num
        self.update()




    
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