import flet as ft


def James(page):
    
    view = ft.View(route="/James",controls=[
                                            
                                            ft.AppBar(title=ft.Text("James"), bgcolor='blue'),
                                            ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                                        ],bgcolor='#ffffff'
                )
    return view