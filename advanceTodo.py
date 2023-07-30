import flet as ft
import sqlite3

dbase = sqlite3.Connection("database.db")
cursor = dbase.cursor()



def main(page: ft.Page):
    page.window_width = 410
    page.window_height = 760

    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = ft.transform.Scale(
            0.8, alignment=ft.alignment.center_right
        )
        page.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = ft.transform.Scale(
            1, alignment=ft.alignment.center_right
        )
        page.update()
    def add_to_db(self):
        task = create_task_view.content.controls[2].content.controls[0].value
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        username VARCHAR(250)
        );  
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tASKS (
        id INTEGER PRIMAKY KEY,
        task VARCHAR(255),
        date_created DATETIME DEFAULT (NOW()),
        poster_id INTEGER,
        FOREIGN KEY (poster_id) REFERENCES users (id)
                   );
               """)
        cursor.execute(f"""
            INSERT INTO tasks (
                id, 
                task, 
                date_created, 
                poster_id
                ) 
                VALUES (task={task},)
            
               """)

    tasks = ft.Column(height=300, scroll="auto",)
    for i in range(10):
        tasks.controls.append(
            ft.Container(
                height=70,
                width=400,
                bgcolor=BG,
                border_radius=15,
                content=ft.Row(
                    controls=[
                        ft.Checkbox(
                            value=False,
                            check_color=PINK,
                            label="Create interesting apps with flet",
                        )
                    ]
                ),
            ),
        )

    create_task_view = ft.Container(
        width=400,
        height=750,
        bgcolor=FG,
        border_radius=25,
        content=ft.Column(
            controls=[
                ft.Container(
                    on_click=lambda _: page.go("/"),
                    height=40,
                    width=40,
                    margin=5,
                    content=ft.IconButton(icon=ft.icons.CLOSE),
                ),
                ft.Container(height=30),
                ft.Container(
                    margin=5,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.TextField(),
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_to_db),
                        ],
                    ),
                ),
                ft.Container(height=30),
                ft.Container(
                    margin=5,
                    content=ft.Container(
                        content=
                            tasks
                            
                    ),
                ),
            ]
        ),
    )

    catrgories_card = ft.Row(scroll="auto")

    categories = ["Business", "Family", "Friends", "Relatives", "Schoolmates"]
    for index, category in enumerate(categories):
        catrgories_card.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("40Tasks"),
                        ft.Text(category),
                        ft.Container(
                            width=160,
                            height=5,
                            bgcolor=ft.colors.WHITE12,
                            border_radius=20,
                            padding=ft.padding.only(right=index * 30),
                            content=ft.Container(bgcolor=PINK),
                        ),
                    ]
                ),
                bgcolor=BG,
                height=110,
                width=170,
                border_radius=20,
                padding=15,
            )
        )

    firstPage_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.MENU,
                                on_click=lambda e: shrink(e),
                            )
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SEARCH),
                                ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED),
                            ]
                        ),
                    ],
                ),
                ft.Container(height=20),
                ft.Text("What's Up, Olivia!"),
                ft.Text("CATEGORIES"),
                ft.Container(
                    padding=ft.padding.only(top=10, bottom=20), content=catrgories_card
                ),
                ft.Container(height=20),
                ft.Text("TODAY'S TASK"),
                ft.Stack(
                    controls=[
                        tasks,
                        ft.FloatingActionButton(
                            bgcolor=PINK,
                            bottom=2,
                            right=20,
                            icon=ft.icons.ADD,
                            on_click=lambda _: page.go("/create_task"),
                        ),
                    ]
                ),
            ]
        )
    )

    secondPage_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.IconButton(
                                        icon=ft.icons.ARROW_BACK_IOS,
                                        on_click=lambda e: restore(e),
                                    )
                                )
                            ]
                        )
                    ],
                ),
                ft.Container(height=20),
                ft.Column(
                    controls=[
                        ft.Container(
                            bgcolor=PINK,
                            width=100,
                            height=100,
                            border_radius=50,
                            padding=3,
                            content=ft.Container(
                                content=ft.Image(
                                    src=f"spider-man.jpg",
                                    width=70,
                                    height=70,
                                    border_radius=50,
                                    fit=ft.ImageFit.FIT_WIDTH,
                                ),
                            ),
                            margin=20,
                        ),
                        ft.Text(
                            "Olivia Mitechele!",
                            size=30,
                        ),
                    ],
                ),
                ft.Text("MENU"),
                ft.Container(
                    margin=20,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.FAVORITE),
                                    ft.Text("Favourite Tasks"),
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.CATEGORY),
                                    ft.Text("Tasks Categories"),
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.ANALYTICS),
                                    ft.Text("Tasks Analytics"),
                                ]
                            ),
                            ft.Container(height=90),
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.IconButton(icon=ft.icons.LOGOUT),
                                            ft.Text("Logout"),
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    ),
                ),
            ]
        )
    )

    page_1 = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(controls=[secondPage_content]),
                padding=ft.padding.only(
                    top=20,
                    left=20,
                    right=20,
                    bottom=5,
                ),
            )
        ]
    )
    page_2 = ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.Container(
                content=ft.Column(controls=[firstPage_content]),
                width=400,
                height=750,
                bgcolor=FG,
                border_radius=25,
                animate=ft.animation.Animation(600, ft.AnimationCurve.DECELERATE),
                animate_scale=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE),
                padding=ft.padding.only(top=20, left=20, right=20, bottom=5),
            )
        ],
    )
    container = ft.Container(
        width=400,
        height=750,
        bgcolor=BG,
        border_radius=25,
        content=ft.Stack(controls=[page_1, page_2]),
    )

    pages = {
        "/": ft.View("/", [container]),
        "/create_task": ft.View("/create_task", [create_task_view]),
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route],
        )

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
