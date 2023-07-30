import flet as ft

def main(page: ft.page):
    page.title = "Flet Calculator"
    page.window_width = 510
    page.window_height = 410
    
    class  CalculatorApp(ft.UserControl):
        def __init__(self):
            super().__init__()
        
        def build(self):
            
            def display(item):
              
                self.textField.value += item
                self.textField.update()
            
            def delete():
                self.textField.value = ''
                self.textField.update()
                
            def calculate():
                result = ''
                try:
                    result = eval(self.textField.value)
                    self.textField.value = str(result)
                except:
                    result = "error"
                    self.textField.value = result
                self.textField.update()
                
            # buttons
            self.button_del = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.RED, icon=ft.icons.DELETE, on_click=lambda _: delete()), width=90
            )
            self.button_left_brace = ft.Container(
                content=ft.FloatingActionButton(text="(", on_click=lambda e: display("(")), width=90
            )
            self.button_right_brace = ft.Container(
                content=ft.FloatingActionButton(text=")",on_click=lambda e: display(")")), width=90
            )
            self.button_dev = ft.Container(content=ft.FloatingActionButton(text="/", on_click=lambda e: display("/")), width=90)
            self.button_add = ft.Container(
                content=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=lambda e: display("+")), width=90
            )
            self.button_minus = ft.Container(content=ft.FloatingActionButton(text="-", on_click=lambda e: display("-")), width=90)
            self.button_pi = ft.Container(content=ft.FloatingActionButton(text="ANS", on_click=lambda e: display("ans")), width=90)
            self.button_zero = ft.Container(content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="0", on_click=lambda e: display("0")), width=90)
            self.button_period = ft.Container(content=ft.FloatingActionButton(text=".", on_click=lambda e: display(".")), width=90)
            self.button_mod = ft.Container(content=ft.FloatingActionButton(text="%", on_click=lambda e: display("%")), width=90)
            self.button_mult = ft.Container(content=ft.FloatingActionButton(text="*", on_click=lambda e: display("*")), width=90)
            self.button_at = ft.Container(content=ft.FloatingActionButton(text="@", on_click=lambda e: display("@")), width=90)
            self.button_less = ft.Container(content=ft.FloatingActionButton(text="<", on_click=lambda e: display("<")), width=90)
            self.button_large = ft.Container(content=ft.FloatingActionButton(text=">", on_click=lambda e: display(">")), width=90)
            self.button_equal = ft.Container(
                content=ft.FloatingActionButton(text="=",bgcolor=ft.colors.ORANGE, on_click=lambda e: calculate()), width=90, height=128
            )

            self.button1 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="1", on_click=lambda e: display("1")),
                width=90,
            )
            self.button2 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="2", on_click=lambda e: display("2")),
                width=90,
            )
            self.button3 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="3", on_click=lambda e: display("3")),
                width=90,
            )
            self.button4 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="4", on_click=lambda e: display("4")),
                width=90,
            )
            self.button5 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="5", on_click=lambda e: display("5")),
                width=90,
            )
            self.button6 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="6", on_click=lambda e: display("6")),
                width=90,
            )
            self.button7 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="7", on_click=lambda e: display("7")),
                width=90,
            )
            self.button8 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="8", on_click=lambda e: display("8")),
                width=90,
            )
            self.button9 = ft.Container(
                content=ft.FloatingActionButton(bgcolor=ft.colors.BROWN, text="9", on_click=lambda e: display("9")),
                width=90,
            )
            
            # columns
            buttonsColumn1 = ft.Column(
                controls=[self.button_del, self.button7, self.button4, self.button1, self.button_period ]
            )
            buttonsColumn2 = ft.Column(
                controls=[self.button_left_brace, self.button8, self.button5, self.button2, self.button_zero]
            )
            buttonsColumn3 = ft.Column(
                controls=[self.button_right_brace, self.button9, self.button6, self.button3, self.button_mod]
            )
            buttonsColumn4 = ft.Column(
                controls=[self.button_dev, self.button_add, self.button_minus, self.button_mult, self.button_pi]
            )
            buttonsColumn5 = ft.Column(
                controls=[self.button_large, self.button_less, self.button_at, self.button_equal]
            )

            self.textField = ft.TextField(width=page.window_width-20)
        
                
            self.button1 = ft.FloatingActionButton(text="1")
            
            self.topView = ft.Row(controls=[
                self.textField
            ])
            
            self.btnView = ft.Container(ft.Row(
                controls=[
                    buttonsColumn1,
                    buttonsColumn2,
                    buttonsColumn3,
                    buttonsColumn4,
                    buttonsColumn5,
                ]
            ))
            
            self.body = ft.Container(
                content=ft.Column(controls=[
                    self.topView,self.btnView
                ])
            )
            return self.body
    
    page.add(CalculatorApp())
ft.app(target=main)
