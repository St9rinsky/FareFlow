import flet as ft
from Frontend.main_page import main_page
def main(page: ft.Page):
    page.title = "FareFlow"
    page.bgcolor = "#000000"

    is_on_desktop = page.platform in [
        ft.PagePlatform.WINDOWS,
        ft.PagePlatform.LINUX,
        ft.PagePlatform.MACOS
    ]

    if is_on_desktop:
        page.window.width = 500
        page.window.height = 900
        page.window.resizable = True
        page.window.center()

    View = ft.Column(expand=True)

    def show_screen(screen):
        View.controls.clear()
        View.controls.append(screen)
        page.update()

    # -----------------------------
    # REUSABLE COMPONENTS
    # -----------------------------
    def app_header(title):
        return ft.Text(
            title,
            size=20,
            weight=ft.FontWeight.BOLD
        )

    def primary_button(text, on_click):
        return ft.Button(
            text,
            width=200,
            on_click=on_click
        )

    # -----------------------------
    # SCREENS
    # -----------------------------

    # HOME SCREEN
    # def home_screen():
    #     return ft.Column(
    #         expand=True,
    #         alignment=ft.MainAxisAlignment.START,
    #         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #         controls=[
    #             ft.AppBar(title=ft.Text("FareFlow")),
    #             app_header("FareFlow"),
    #             ft.Text("Home Screen"),
    #             primary_button("Go to Payment", lambda e: show_screen(payment_screen())),
    #         ]
    #     )
 
    # PAYMENT SCREEN
    def payment_screen():
        amount = ft.TextField(label="Amount", read_only=True)

        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.AppBar(title=ft.Text("FareFlow")),
                app_header("Payment"),
                amount,
                primary_button("Back", lambda e: show_screen(main_page)),
            ]
        )

    # -----------------------------
    # MOBILE FRAME (DESKTOP ONLY)
    # -----------------------------
    app_layout = ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE,
        padding=20,
        content=View
    )

    if is_on_desktop:
        page.add(
            ft.Row(
                [
                    ft.Container(
                        width=390,
                        height=844,
                        border_radius=30,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        bgcolor=ft.Colors.WHITE,
                        content=app_layout,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    else:
        page.add(app_layout)

    # -----------------------------
    # START APP
    # -----------------------------
    show_screen(main_page(page))
    page.update()

ft.app(target=main)