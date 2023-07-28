import flet as ft

class TaskApp(ft.UserControl):
    def build(self):
        self.textFlield = ft.TextField(width=350)
        self.addBtn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.addClick)
        self.tasks = ft.Column()
        taskArea = ft.Column(
            controls=[ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[self.textFlield, self.addBtn]), self.tasks]
        )
        return taskArea

    def addClick(self, e):
        task = Task(self.textFlield.value, self.taskDelete)
        if self.textFlield.value != '':
            self.tasks.controls.append(task)
            self.textFlield.value=''
            self.update()

    def taskDelete(self, task):
        self.tasks.controls.remove(task)
        self.update()
        
    

class Task(ft.UserControl):
    def __init__(self, taskName, taskDelete):
        super().__init__()
        self.taskName = taskName
        self.taskDelete = taskDelete

    def build(self):
        self.displayTask = ft.Checkbox(label=self.taskName, value=False, on_change=self.checkBoxTrue)
        self.editName = ft.TextField()
        self.displayView = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.displayTask,
                ft.Row( controls=[
                    ft.IconButton(ft.icons.CREATE_OUTLINED,
                                  on_click=self.editClick),
                    ft.IconButton(ft.icons.DELETE_OUTLINED,
                                  on_click=self.deleteClick)
                    ]),
            ]
        )
        self.editView = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, visible=False, controls=[self.editName,
                                         ft.IconButton(ft.icons.DONE_OUTLINED,
                                  on_click=self.saveClick)
                                         ])
        return ft.Column(controls=[self.displayView,  self.editView])
    
    def checkBoxTrue(self, e):
        self.displayTask.value  = True
        
    def saveClick(self, e):
        self.displayView=True
        self.editView.visible = False
        self.displayTask.label=self.editName.value
        self.update()
        
    def editClick(self, e):
        self.displayView=False
        self.editView.visible = True
        self.editName.value = self.displayTask.label
        self.update()
        
    def deleteClick(self, e):
        if self.displayTask.value == True:
            self.taskDelete(self)


def main(page: ft.page):
    page.title = "To Do app With Classes"
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "grey"

    page.add(TaskApp())
    page.update


ft.app(target=main)
