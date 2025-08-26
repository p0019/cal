import flet as ft

def main(page: ft.Page):
    page.title = "เครื่องคิดเลขสวยงาม"
    page.window_width, page.window_height = 350, 550
    page.window_resizable = False
    page.bgcolor = "#f0f2f5"

    first_number, operator = None, None

    display = ft.TextField(
        value="0", text_align=ft.TextAlign.RIGHT, read_only=True,
        height=80, border_color="transparent", bgcolor="#ffffff",
        border_radius=15, text_style=ft.TextStyle(size=40, weight=ft.FontWeight.W_400),
        content_padding=ft.padding.symmetric(horizontal=20)
    )

    def button_clicked(e):
        nonlocal first_number, operator
        data = e.control.data
        try:
            if data.isdigit():
                display.value = data if display.value in ["0", "Error"] else display.value + data
            elif data in "+-*/":
                first_number, operator, display.value = float(display.value), data, "0"
            elif data == "=" and first_number is not None and operator:
                second = float(display.value)
                if operator == "/" and second == 0:
                    display.value = "Error"
                else:
                    result = eval(f"{first_number}{operator}{second}")
                    display.value = str(int(result)) if result.is_integer() else str(result)
                first_number = operator = None
            elif data == "C":
                first_number = operator = None
                display.value = "0"
        except:
            display.value = "Error"
        page.update()

    def create_button(text, data, bgcolor, color="white"):
        return ft.ElevatedButton(
            text=text, data=data, on_click=button_clicked, expand=True, height=65,
            style=ft.ButtonStyle(
                bgcolor=bgcolor, color=color,
                shape=ft.RoundedRectangleBorder(radius=50),  # ปุ่มวงกลมโค้งๆ
                elevation=4,
                overlay_color="white10"
            )
        )

    # layout ปุ่ม
    buttons = [
        [("7","7","#424242"), ("8","8","#424242"), ("9","9","#424242"), ("/","/","#ff9f0a")],
        [("4","4","#424242"), ("5","5","#424242"), ("6","6","#424242"), ("*","*","#ff9f0a")],
        [("1","1","#424242"), ("2","2","#424242"), ("3","3","#424242"), ("-","-","#ff9f0a")],
        [("C","C","#d32f2f"), ("0","0","#424242"), ("=","=","#ff9f0a"), ("+","+", "#ff9f0a")]
    ]

    rows = [ft.Row([create_button(t,d,c) for t,d,c in row], spacing=10) for row in buttons]

    calculator = ft.Container(
        width=320, padding=20, border_radius=20, bgcolor="#ffffff",
        shadow=ft.BoxShadow(blur_radius=20, color="black12", offset=ft.Offset(0,8)),
        content=ft.Column([display] + rows, spacing=15)
    )

    # --- จัดให้อยู่กลางจอ ---
    page.add(
        ft.Container(
            content=calculator,
            alignment=ft.alignment.center,
            expand=True
        )
    )

ft.app(target=main)
