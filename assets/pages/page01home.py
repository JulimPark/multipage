import flet as ft


def view_homepage(page):
    
    title = ft.Text(value='PRAY & CRY',size=60,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=0),text_align=ft.TextAlign.CENTER)
    prayHands = ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/mdi--hands-pray.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9tZGktLWhhbmRzLXByYXkucG5nIiwiaWF0IjoxNzQxNjMyODcyLCJleHAiOjE3NzMxNjg4NzJ9.fRNPJTFObYox9F8AytUlfdh--ytlz-rWgsx86tUVYEg',width=30,height=30)
    header01 = ft.Text(value="Dear My Father",size=20,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=0),text_align=ft.TextAlign.CENTER)
    textfiled01 = ft.TextField(label='My Prayer',hint_text='Dear Heavenly Father...',max_lines=5,color='#141F64',border_color='#141F64',width=380,multiline=True,cursor_color='#1024C6',cursor_radius=10,cursor_width=10,label_style=ft.TextStyle(color='#9E9E9E'),bgcolor='#FBFCFD',hint_fade_duration=500)
    
    header01Col = ft.Column(controls=[ft.Row(controls=[prayHands,header01]),textfiled01],horizontal_alignment=ft.CrossAxisAlignment.START,width=380,)
    mainColumn = ft.Container(content=ft.Column(controls=[
        title,
        header01Col,
    ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO),alignment=ft.alignment.top_center)
    view = ft.View(route="/",controls=[
                                            mainColumn,
                                            ft.AppBar(title=ft.Text("Home"), bgcolor='blue'),
                                            ft.ElevatedButton("Go James", on_click=lambda _: page.go("/James")),
                                        ],bgcolor='#ffffff'
                )
    return view