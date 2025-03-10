import flet as ft

def main(page):
    page.title = "super clicker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    count_text = ft.Text("Clicks: 0", size=100)

    def button_click(e):
        count_text.value = f"clicks: {int(count_text.value.split(': ')[1]) + 1}"
        page.update()

    def reset_click(e):
        count_text.value = "clicks: 0"
        page.update()

    page.add(
        count_text,
        ft.Row([ft.ElevatedButton("click me!", on_click=button_click)], alignment=ft.MainAxisAlignment.CENTER),
        ft.ElevatedButton("reset", on_click=reset_click),
    )
ft.app(main)