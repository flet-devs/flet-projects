import flet as ft


class  CalculatorApp(ft.UserControl):
    def build(self):
        self.textField = ft.TextField(width=490)
        topView = ft.Row(controls=[
            self.textField
        ])
        return topView

def main(page: ft.page):
    page.title = "Flet Calculator"
    page.window_width = 510
    page.window_height = 410
    
    page.add(CalculatorApp())
ft.app(target=main)














    # def display(item):
    #     textField.value(item)
    #     print(textField.value)

    # # buttons
    # button_del = ft.Container(
    #     content=ft.FloatingActionButton(icon=ft.icons.DELETE), width=90
    # )
    # button_left_brace = ft.Container(
    #     content=ft.FloatingActionButton(text="("), width=90
    # )
    # button_right_brace = ft.Container(
    #     content=ft.FloatingActionButton(text=")"), width=90
    # )
    # button_dev = ft.Container(content=ft.FloatingActionButton(text="/"), width=90)
    # button_add = ft.Container(
    #     content=ft.FloatingActionButton(icon=ft.icons.ADD), width=90
    # )
    # button_minus = ft.Container(content=ft.FloatingActionButton(text="-"), width=90)
    # button_pi = ft.Container(content=ft.FloatingActionButton(text="pi"), width=90)
    # button_zero = ft.Container(content=ft.FloatingActionButton(text="0"), width=90)
    # button_period = ft.Container(content=ft.FloatingActionButton(text="."), width=90)
    # button_mod = ft.Container(content=ft.FloatingActionButton(text="%"), width=90)
    # button_mult = ft.Container(content=ft.FloatingActionButton(text="*"), width=90)
    # button_at = ft.Container(content=ft.FloatingActionButton(text="@"), width=90)
    # button_less = ft.Container(content=ft.FloatingActionButton(text="<"), width=90)
    # button_large = ft.Container(content=ft.FloatingActionButton(text=">"), width=90)
    # button_equal = ft.Container(
    #     content=ft.FloatingActionButton(text="="), width=90, height=128
    # )

    # button1 = ft.Container(
    #     content=ft.FloatingActionButton(text="1", on_click=lambda e: display("1")),
    #     width=90,
    # )
    # button2 = ft.Container(
    #     content=ft.FloatingActionButton(text="2", on_click=lambda e: display("2")),
    #     width=90,
    # )
    # button3 = ft.Container(
    #     content=ft.FloatingActionButton(text="3", on_click=lambda e: display("3")),
    #     width=90,
    # )
    # button4 = ft.Container(
    #     content=ft.FloatingActionButton(text="4", on_click=lambda e: display("4")),
    #     width=90,
    # )
    # button5 = ft.Container(
    #     content=ft.FloatingActionButton(text="5", on_click=lambda e: display("5")),
    #     width=90,
    # )
    # button6 = ft.Container(
    #     content=ft.FloatingActionButton(text="6", on_click=lambda e: display("6")),
    #     width=90,
    # )
    # button7 = ft.Container(
    #     content=ft.FloatingActionButton(text="7", on_click=lambda e: display("7")),
    #     width=90,
    # )
    # button8 = ft.Container(
    #     content=ft.FloatingActionButton(text="8", on_click=lambda e: display("8")),
    #     width=90,
    # )
    # button9 = ft.Container(
    #     content=ft.FloatingActionButton(text="9", on_click=lambda e: display("9")),
    #     width=90,
    # )

    # # columns
    # buttonsColumn1 = ft.Column(
    #     controls=[button_del, button7, button4, button1, button_zero]
    # )
    # buttonsColumn2 = ft.Column(
    #     controls=[button_left_brace, button8, button5, button2, button_period]
    # )
    # buttonsColumn3 = ft.Column(
    #     controls=[button_right_brace, button9, button6, button3, button_mod]
    # )
    # buttonsColumn4 = ft.Column(
    #     controls=[button_dev, button_add, button_minus, button_mult, button_pi]
    # )
    # buttonsColumn5 = ft.Column(
    #     controls=[button_large, button_less, button_at, button_equal]
    # )

    # buttonRow = ft.Row(
    #     controls=[
    #         buttonsColumn1,
    #         buttonsColumn2,
    #         buttonsColumn3,
    #         buttonsColumn4,
    #         buttonsColumn5,
    #     ]
    # )

    # # render
    # page.add(textField, buttonRow)



