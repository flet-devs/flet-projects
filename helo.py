import flet

def main (page: flet.Page):
    page.title = "hello"
    
    text = flet.Text("Hllo world",  color="red")
    text2 = flet.Text("This is another text", color="green")
    page.controls.append(text)
    page.controls.append(text2)
    page.update()
flet.app(target=main)