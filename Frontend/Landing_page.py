import flet as ft

def landing(page):
    app_bar = ft.AppBar(
       title = ft.Text("FareFlow"),
       center_title=False,
    )
    layout = ft.Column(
        controls = [
            app_bar
        ]
    )


    return layout