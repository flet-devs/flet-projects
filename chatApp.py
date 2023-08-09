
import flet as ft

class Chat(ft.UserControl):

    def __init__(self):
        super().__init__()

    def build(self):
        self.default_color = "#242325"
        self.popup_color = "#353535"
        self.badge_color = "#ff67ff"

        
        self.members_container=ft.Column(height=500,scroll='auto',)
        for i in range(10):
            self.members_container.controls.append(ft.Container(
                    # bgcolor=ft.colors.RED,
                    padding=ft.padding.only(top=5),
                content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
             col={
                "xl":10
            },
            controls=[
            ft.ResponsiveRow(
            controls=[
                ft.Column(
            col={
                "xl":2
            },
            controls=[
            ft.CircleAvatar(
            foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
            content=ft.Text("RR"),
                    )
            ],
                ),
                ft.Column(
             col={
                "xl":4
            },
            controls=[
            ft.Column(
            
            # col={
            #     "xl":3
            # },
            controls=[

            ft.Text("Ronald Richards"),
            ft.Text("Typing....")
            ],
                    )
            ],
                )
            ]
            )
            ],
           
                    ),


                    ft.Column(
            alignment=ft.MainAxisAlignment.END,
            col={
                "xl":2
            },
            controls=[
                        ft.Column(
            
            controls=[

            ft.Text("430pm"),
            ft.Container(
                
                bgcolor=self.badge_color,
                border_radius=10,
                height=20,
                width=20,
                padding=ft.padding.only(top=0,left=5,right=5,bottom=5),
                content=ft.Text("3")),
            
            ],
                    )
                    ]),
                    ])
                    ),)

        #first app bar
        self.appBarStart = ft.Container(
        content=ft.NavigationRail(
        bgcolor=self.default_color,
            leading=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("Messages",size=18, weight='bold', col={"xl":4}),
                ft.IconButton(ft.icons.FILTER_3, col={"xl":4}),

                ft.Column(controls=[
                ft.Divider(),
                ft.TextField(label="search", icon=ft.icons.SEARCH, border_radius=25,),
                ft.Container(height=10),
                self.members_container
                    
                ]),
           
        ],),
         height=700,
        # extended=True,
        ),
    )
        #second app bar
        self.appBarMiddle = ft.Container(
            
        bgcolor=self.default_color,
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
            ft.Container(
            padding=5,
            col={
                "xl":6
            },
            content=ft.ResponsiveRow(
            controls=[
                ft.CircleAvatar(
            col={
                "xl":5
            },
                bgcolor=ft.colors.BLUE,
                content=ft.Text("FF")),
                ft.Column(
            col={
                "xl":7
            },
            controls=[ft.Text("Annabel White",size=18, weight='bold'),
                      ft.Text("Online",size=13, )
                ]),
            ]),
                ),
            
            ft.Container(
            padding=5,
            col={
                "xl":2,
            },
            content=ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(icon=ft.icons.INFO_OUTLINED,text="Info",),
                    ft.PopupMenuItem(icon=ft.icons.DELETE_OUTLINE_OUTLINED,text="Delete"), 
                    ft.PopupMenuItem(icon=ft.icons.REPORT_PROBLEM_OUTLINED,text="Report"),  
                    ft.PopupMenuItem(icon=ft.icons.WB_SUNNY_OUTLINED,text="Style"), 
                   
                ]
            ),)
            
            
        ],)
    )  
    
        #third app bar    
        self.appBarEnd = ft.Container(
        bgcolor=self.default_color,
        
        content=ft.Column(controls=[
            
             ft.NavigationRail(
            height=700,
            leading=ft.ResponsiveRow(
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
            ft.Text("Info",size=18, weight='bold'),
                # ft.Container(height=9),
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
                                    src=f"spider-man.jpg",
                                    width=70,
                                    height=70,
                                    border_radius=50,
                                    fit=ft.ImageFit.FIT_WIDTH,
                                ),
                            ),
                            
                        ),
                        ft.Text("Annabel White",size=18, weight='bold'),
                        ft.Text("7,876 trips | Joined Sep 2022",size=13, weight='light'),
                        ft.OutlinedButton(text="View profile")
            ],
            
            ),
              
            ]
        ),
        ),
        ])
       
        
    )
        
        #initialize body
        self.body = ft.ResponsiveRow(
            controls=[
                ft.Column(
            col={
                "xl":4
            },
            controls=[
                    self.appBarStart,
                ]),
                ft.Column(
            col={
                "xl":5
            },
            controls=[
                    self.appBarMiddle,
                ]),
                ft.Column(
            col={
                "xl":3
            },
            controls=[
                    self.appBarEnd,
                ])
            ]
        )

        return self.body 

def main(page=ft.Page):
    page.title = "Flet chat app"


    page.add(Chat())

ft.app(target=main)
