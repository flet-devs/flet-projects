import flet as ft

def main(page: ft.Page):
    page.title="Flet Dashboard"
    page.event_handlers.get
    print(page.on_resize.count)
    screenWidth = page.window_width
    if screenWidth <= 700.0:
        page.bgcolor = "red"
                
    elif screenWidth > 700.0 and screenWidth <= 1400.0:
        page.bgcolor = "green"
    else:
        page.bgcolor = "blue"
        
        
    #for responsive screen on all platform
    class ResponsiveScreen(ft.UserControl):
        def __init__(self):
            super().__init__()
            
        def build(self):
            self.screenWidth = page.window_width
            self.text = ft.Text(self.screenWidth)
            
                
            
            taskArea = ft.Column(
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[self.text,]
                        )
                    ]
                )
            return taskArea
    
    page.add(ResponsiveScreen())
    
ft.app(target=main)