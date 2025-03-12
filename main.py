import flet as ft
from assets.pages.page01home import view_homepage
from assets.pages.page02test import James
def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
                    
        if page.route == "/":
            viewHome = view_homepage(page)
            page.views.append(viewHome)
        
        if page.route == "/James":
            viewHome = James(page)
            page.views.append(viewHome)
        
        
        page.update()

    # def view_pop(view):
    #     print('popping')
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    page.on_route_change = route_change
    # page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)