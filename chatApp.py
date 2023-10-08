import flet as ft

class Chat(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        # Define colors as constants
        DEFAULT_COLOR = "#242325"
        BADGE_COLOR = "#ff67ff"

        # Create a container for members
        members_container = ft.Column(height=500, scroll='auto')
        for i in range(10):
            # Create member containers
            member_container = ft.Container(
                padding=ft.padding.only(top=5),
                content=ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            col={"xl": 10},
                            controls=[
                                ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(
                                            col={"xl": 2},
                                            controls=[
                                                ft.CircleAvatar(
                                                    foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
                                                    content=ft.Text("RR")
                                                )
                                            ]
                                        ),
                                        ft.Column(
                                            col={"xl": 4},
                                            controls=[
                                                ft.Text("Ronald Richards"),
                                                ft.Text("Typing....")
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.END,
                            col={"xl": 2},
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text("430pm"),
                                        ft.Container(
                                            bgcolor=BADGE_COLOR,
                                            border_radius=10,
                                            height=20,
                                            width=20,
                                            padding=ft.padding.only(top=0, left=5, right=5, bottom=5),
                                            content=ft.Text("3")
                                        ),
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
            members_container.controls.append(member_container)

        # First app bar
        app_bar_start = ft.Container(
            content=ft.NavigationRail(
                bgcolor=DEFAULT_COLOR,
                leading=ft.ResponsiveRow(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("Messages", size=18, weight='bold', col={"xl": 4}),
                        ft.IconButton(ft.icons.FILTER_3, col={"xl": 4}),
                        ft.Column(controls=[
                            ft.Divider(),
                            ft.TextField(label="search", icon=ft.icons.SEARCH, border_radius=25),
                            ft.Container(height=10),
                            members_container
                        ]),
                    ]
                ),
                height=700
            )
        )

        # Second app bar
        app_bar_middle = ft.Container(
            bgcolor=DEFAULT_COLOR,
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Container(
                        padding=5,
                        col={"xl": 6},
                        content=ft.ResponsiveRow(
                            controls=[
                                ft.CircleAvatar(
                                    col={"xl": 5},
                                    bgcolor=ft.colors.BLUE,
                                    content=ft.Text("FF")
                                ),
                                ft.Column(
                                    col={"xl": 7},
                                    controls=[
                                        ft.Text("Annabel White", size=18, weight='bold'),
                                        ft.Text("Online", size=13),
                                    ]
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        padding=5,
                        col={"xl": 2},
                        content=ft.PopupMenuButton(
                            items=[
                                ft.PopupMenuItem(icon=ft.icons.INFO_OUTLINED, text="Info"),
                                ft.PopupMenuItem(icon=ft.icons.DELETE_OUTLINE_OUTLINED, text="Delete"),
                                ft.PopupMenuItem(icon=ft.icons.REPORT_PROBLEM_OUTLINED, text="Report"),
                                ft.PopupMenuItem(icon=ft.icons.WB_SUNNY_OUTLINED, text="Style"),
                            ]
                        ),
                    )
                ]
            )
        )

        # Third app bar
        app_bar_end = ft.Container(
            bgcolor=DEFAULT_COLOR,
            content=ft.Column(controls=[
                ft.NavigationRail(
                    height=700,
                    leading=ft.ResponsiveRow(
                        controls=[
                            ft.Text("Info", size=18, weight='bold'),
                            ft.Divider(),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        bgcolor=ft.colors.PINK,
                                        width=100,
                                        height=100,
                                        border_radius=50,
                                        padding=3,
                                        content=ft.Container(
                                            content=ft.Image(
                                                src="spider-man.jpg",
                                                width=70,
                                                height=70,
                                                border_radius=50,
                                                fit=ft.ImageFit.FIT_WIDTH,
                                            ),
                                        ),
                                    ),
                                    ft.Text("Annabel White", size=18, weight='bold'),
                                    ft.Text("7,876 trips | Joined Sep 2022", size=13, weight='light'),
                                    ft.OutlinedButton(text="View profile")
                                ]
                            ),
                        ]
                    ),
                ),
            ])
        )

        # Initialize body
        body = ft.ResponsiveRow(
            controls=[
                ft.Column(col={"xl": 4}, controls=[app_bar_start]),
                ft.Column(col={"xl": 5}, controls=[app_bar_middle]),
                ft.Column(col={"xl": 3}, controls=[app_bar_end]),
            ]
        )

        return body


def main(page=ft.Page):
    page.title = "Flet chat app"
    page.add(Chat())


ft.app(target=main)
