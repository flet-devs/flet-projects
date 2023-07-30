import flet as ft


class DashApp(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        for colItem in range(10):
            pass
        self.body = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    col={
                        "xs":0,
                        "sm": 4,
                        "md": 4,
                        "xl": 4,
                    },
                    border_radius=20,
                    content=ft.NavigationRail(
                        bgcolor=ft.colors.GREY,
                        selected_index=0,
                        label_type=ft.NavigationRailLabelType.ALL,
                        extended=True,
                        height=800,
                        leading=ft.Container(
                            padding=ft.padding.only(right=5, left=5, bottom=35, top=35),
                            content=ft.Icon(
                                name=ft.icons.FAVORITE, size=50,
                            ),
                        ),
                        
                        destinations=[
                            ft.NavigationRailDestination(
                                padding=5,
                                icon=ft.icons.DASHBOARD_OUTLINED,
                                selected_icon=ft.icons.DASHBOARD,
                                label="D A S H B O A R D",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.icons.SETTINGS_OUTLINED,
                                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                                label_content=ft.Text("S E T T I N G S"),
                            ),
                            ft.NavigationRailDestination(
                                icon_content=ft.Icon(ft.icons.TAG_OUTLINED),
                                selected_icon_content=ft.Icon(ft.icons.TAG),
                                label="A B O U T",
                            ),
                            ft.NavigationRailDestination(
                                icon_content=ft.Icon(ft.icons.LOGOUT_OUTLINED),
                                selected_icon_content=ft.Icon(ft.icons.LOGOUT),
                                label="L O G O U T",
                            ),
                        ],
                    ),
                ),
                ft.Column(
                    scroll="auto",
                    col={
                        "xs":11,
                        "sm": 8,
                        "md": 6,
                        "xl": 6,
                    },
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    col={
                                        "sm": 6,
                                        "md": 3,
                                    },
                                    border_radius=10,
                                    padding=ft.padding.only(top=70,bottom=70),
                                    bgcolor=ft.colors.GREY,
                                    
                                ),
                                ft.Container(
                                    col={
                                        "sm": 6,
                                        "md": 3,
                                    },
                                    border_radius=10,
                                    padding=ft.padding.only(top=70,bottom=70),
                                    bgcolor=ft.colors.GREY,
                                    
                                ),
                                ft.Container(
                                    col={
                                        "sm": 6,
                                        "md": 3,
                                    },
                                    border_radius=10,
                                    padding=ft.padding.only(top=70,bottom=70),
                                    bgcolor=ft.colors.GREY,
                                    
                                ),
                                ft.Container(
                                    col={
                                        "sm": 6,
                                        "md": 3,
                                    },
                                    border_radius=10,
                                    padding=ft.padding.only(top=70,bottom=70),
                                    bgcolor=ft.colors.GREY,
                                    
                                ),
                            ]
                        ),
                        ft.ResponsiveRow(
                            
                            controls=[
                                 ft.Column(
                           scroll="auto",
                            controls=[
                            
                                ft.Container(
                         
                            border_radius=10,
                            padding=ft.padding.only(top=50,bottom=50,),
                            bgcolor=ft.colors.WHITE,
                           ),
                                ft.Container(
                         
                            border_radius=10,
                            padding=ft.padding.only(top=50,bottom=50,),
                            bgcolor=ft.colors.WHITE,
                           ),
                        ft.Container(
                         
                            border_radius=10,
                            padding=ft.padding.only(top=50,bottom=50,),
                            bgcolor=ft.colors.WHITE,
                            ),
                        ft.Container(
                         
                            border_radius=10,
                            padding=ft.padding.only(top=50,bottom=50,),
                            bgcolor=ft.colors.WHITE,
                            ),
                        ft.Container(
                         
                            border_radius=10,
                            padding=ft.padding.only(top=50,bottom=50,),
                            bgcolor=ft.colors.WHITE,
                            ),
                         ft.Container(
                         
                            border_radius=10,
                            padding=ft.padding.only(top=50,bottom=50,),
                            bgcolor=ft.colors.WHITE,
                            ),
                                ]),
                        
                                ]),
                       
                    ],
                    
                ),
                ft.Column(
                    alignment=ft.MainAxisAlignment.END,
                     col={
                        "sm": 0,
                        "md": 2,
                        "xl": 2,
                    },
                    controls=[
                        ft.Container(
                            height=350,
                            border_radius=20,
                            bgcolor=ft.colors.GREY,
                            
                        ),
                        ft.Container(
                            height=350,
                            border_radius=20,
                            bgcolor=ft.colors.WHITE,
                            
                        )
                    ]
                ),
                
            ]
        )

        return self.body


def main(page: ft.Page):
    page.title = "Flet Responsive"
    page.bgcolor = ft.colors.GREY_300

    page.add(DashApp())


ft.app(target=main)
