import flet as ft 

def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width = 300
    page.window_height = 350

    operand = 0
    subOperand = 0
    ans = 0
    result = ft.Text(value=f"{ans}",expand=4,height=50)

    page.add(
        ft.Row(controls=[result]),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC",expand=1),
                ft.ElevatedButton(text="+/-",expand=1),
                ft.ElevatedButton(text="%",expand=1),
                ft.ElevatedButton(text="/", expand=1),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7",expand=1),
                ft.ElevatedButton(text="8", expand=1),
                ft.ElevatedButton(text="9",expand=1),
                ft.ElevatedButton(text="*", expand=1),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", expand=1),
                ft.ElevatedButton(text="5", expand=1),
                ft.ElevatedButton(text="6", expand=1),
                ft.ElevatedButton(text="-", expand=1),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1",expand=1),
                ft.ElevatedButton(text="2", expand=1),
                ft.ElevatedButton(text="3",expand=1),
                ft.ElevatedButton(text="+", expand=1),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="0",expand=2),
                ft.ElevatedButton(text=".",expand=1),
                ft.ElevatedButton(text="=", expand=1),
            ]
        ),
    )

ft.app(target=main)