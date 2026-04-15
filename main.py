import flet as ft

def main(page: ft.Page):
    page.title = "FareFlow"

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

    def landing(page):
        app_bar = ft.AppBar(
        title = ft.Text("FareFlow"),
        center_title=True,
        )

        price_input = ft.TextField(
            hint_text= "Enter fare price in Rands",
            text_align=ft.TextAlign.CENTER,
            input_filter=ft.NumbersOnlyInputFilter(),


        )

        layout = ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [
                app_bar,
                price_input,
                primary_button("Start session",lambda e: show_screen(session_page(page)))

            ]
        )


        return layout
    

    def get_appbar(page):

        Home = ft.IconButton(
            icon = ft.Icons.HOME,
            on_click =lambda e: e
        )

        Wallet = ft.IconButton(
            icon = ft.Icons.MONEY,
            on_click =lambda e: e
        )

        Swap = ft.IconButton(
            icon = ft.Icons.SWAP_HORIZ,
            on_click = lambda e: e
        )

        info = ft.IconButton(
            icon = ft.Icons.INFO_OUTLINE,
            badge=ft.Badge(label="1",bgcolor="BLUE"),
            on_click= lambda e: e
        )
        close = ft.IconButton(
            icon = ft.Icons.CLOSE,
            on_click= lambda e: e
        )

        app_bar = ft.AppBar(
            title = ft.Text("FareFlow",weight=ft.FontWeight.W_900,color="yellow"),
            actions = [Home,Wallet,Swap,info,close]
        )

        return app_bar
 
    # PAYMENT SCREEN
    def session_page(page):
        app_bar = get_appbar(page)
        price_view = ft.TextField(
            value = "Fare cost: from backend",
            text_align=ft.TextAlign.CENTER,
            read_only=True,
        )
        passenger_count = ft.Container(
            width= 200,
            height= 30,
            bgcolor="#000000",
            content =ft.Row(
                ft.Text("passegers")
            )
        )

        summary = ft.Container(
            padding=ft.Padding.symmetric(horizontal=20,vertical=20),
            border_radius=15,
            bgcolor= "#FFFFFF",
            content= ft.Column(
                tight=True,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[ft.Text("Total Passengers",color="BLACK"),ft.Text("Total",color="BLACK")]),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[ft.Text("Total Passengers"),ft.Text("Total")]),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[ft.Text("Total Paid",color="BLACK"),ft.Text("Total",color="BLACK")]),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[ft.Text("Change"),ft.Text("Total")]),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[ft.Text("Result"),ft.Text("Total")])

                ]
            )
        )
        currency_dial = ft.Container(
            height=30,
            bgcolor="#ffffff",
            content= ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                controls = [
                    ft.Text("hello")
                ]
            )
        )


        return ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                app_bar,
                price_view,
                ft.Text("Passegers"),
                passenger_count,
                ft.Text("summary"),
                summary,
                ft.Text("Amount given"),
                currency_dial,
                primary_button("Back", lambda e: show_screen(landing(page))),
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
    show_screen(session_page(page))
    page.update()

ft.run(main)