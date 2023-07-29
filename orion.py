import flet as ft


class TheApp(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.rail = ft.NavigationRail(
            bgcolor="",
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            extended=True,
            height=700,
            min_width=100,
            min_extended_width=200,
            leading=ft.Row(
                
                controls=[
                    ft.Icon(name=ft.icons.ACCESS_TIME_ROUNDED, color=ft.colors.YELLOW),
                    ft.Text(value="ORION"),
                ],
            ),
            destinations=[
                ft.NavigationRailDestination(
                    padding=5,
                    icon=ft.icons.DASHBOARD_OUTLINED,
                    selected_icon=ft.icons.DASHBOARD,
                    label="Dashboard",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                    selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                    label="Second",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ],
        )

        self.topBarRow = ft.Row(
            controls=[
                ft.TextField(bgcolor=ft.colors.WHITE10, border=None),
                ft.Dropdown(
                    options=[
                        ft.dropdown.Option("Red"),
                        ft.dropdown.Option("Green"),
                        ft.dropdown.Option("Blue"),
                    ],
                    label="Monday,25th,October",
                    width=200,
                    border=None,
                ),
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.MAIL_OUTLINE),
                        ft.Icon(name=ft.icons.NOTIFICATIONS_OUTLINED),
                    ]
                ),
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    text="New Board",
                    bgcolor=ft.colors.YELLOW,
                ),
            ],
        )
        self.middleRow = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Row([ft.Text("My NFT Collection")]),
                                    ]
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Text("All"),
                                                    padding=5,
                                                    bgcolor=ft.colors.WHITE10,
                                                    border_radius=10,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("Collection"),
                                                    padding=5,
                                                    bgcolor=ft.colors.WHITE,
                                                    border_radius=10,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("Highest Price"),
                                                    padding=5,
                                                    bgcolor=ft.colors.WHITE10,
                                                    border_radius=10,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("Lowest Price"),
                                                    padding=5,
                                                    bgcolor=ft.colors.WHITE10,
                                                    border_radius=10,
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Image(
                                        src=f"spider-man.jpg",
                                        width=200,
                                        height=300,
                                        fit=ft.ImageFit.FIT_WIDTH,
                                        border_radius=12,
                                    ),
                                    margin=10,
                                ),
                                ft.Container(
                                    content=ft.Image(
                                        src=f"astronaut.jpg",
                                        width=200,
                                        height=300,
                                        fit=ft.ImageFit.FIT_WIDTH,
                                        border_radius=12,
                                    ),
                                    margin=10,
                                ),
                                ft.Container(
                                    content=ft.Image(
                                        src=f"dice.jpg",
                                        width=200,
                                        height=300,
                                        fit=ft.ImageFit.FIT_WIDTH,
                                        border_radius=12,
                                    ),
                                    margin=10,
                                ),
                                ft.Container(
                                    content=ft.Image(
                                        src=f"jupiter.jpg",
                                        width=200,
                                        height=300,
                                        fit=ft.ImageFit.FIT_WIDTH,
                                        border_radius=12,
                                    ),
                                    margin=10,
                                ),
                            ]
                        ),
                    ]
                )
            ]
        )

        self.navSection = ft.Container(
            content=self.rail, padding=7, bgcolor=ft.colors.BLACK87, border_radius=15
        )
        self.topSection = ft.Container(
            content=ft.Column(
                controls=[self.topBarRow],
            ),
            padding=7,
            bgcolor=ft.colors.BLACK87,
            border_radius=15,
        )
        self.middleSection = ft.Container(
            content=ft.Column(
                controls=[self.middleRow],
            ),
            padding=7,
            bgcolor=ft.colors.BLACK87,
            border_radius=15,
        )

        bodyRow = ft.Row(
            alignment="center",
            vertical_alignment="center",
            controls=[
                ft.Container(content= self.navSection,),
                
                ft.VerticalDivider(width=1),
                ft.Column(
                    controls=[
                        self.topSection,
                        ft.Divider(height=20),
                        self.middleSection,
                        ft.Divider(height=20),
                        self.middleSection,
                    ],
                ),
            ]
        )
        return bodyRow


def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY
    page.window_height=700

    page.add(TheApp())


ft.app(target=main)
