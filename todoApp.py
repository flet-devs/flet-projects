import flet  as ft

def main(page: ft.Page):
    
    def addTask(p):
        checkBox = ft.Checkbox(value=False)
        checkBoxText = ft.Text(value=textField.value, width =350, size=15)
        deleteButton = ft.ElevatedButton(text="Delete", on_click=deleteTask)
        taskRow = ft.Row(controls=[checkBox,
                               checkBoxText,
                               deleteButton],
                     alignment=ft.MainAxisAlignment.START)
        textField.value=""
        
        
        page.add(taskRow)
        
    #remove task
    def deleteTask(p):
        
        page.controls.pop()
        page.update()
        
    page.window_width=500
    page.window_height=700
    page.bgcolor="grey"
    textField = ft.TextField(width=380)
    addBtn = ft.FloatingActionButton(icon = ft.icons.ADD, on_click=addTask)
    
    
    entriesRow = ft.Row(controls=[textField,
                                  addBtn], 
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
    page.add(entriesRow)
    
ft.app(target=main)