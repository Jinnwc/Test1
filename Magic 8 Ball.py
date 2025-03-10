import flet as ft
import random

def main(page: ft.Page):
    page.title = "magic 8 ball"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    responses = ["yes, definitely", "no way!", "maybe..."]

    def get_answer(e):
        answer.value = random.choice(responses) if question.value else "Please ask a question first!"
        page.update()

    question = ft.TextField(label="Type your question here", width=300, text_align=ft.TextAlign.CENTER)
    answer = ft.Text(value="Your answer will appear here...", size=20, text_align=ft.TextAlign.CENTER)

    page.add(ft.Column(
    [question, ft.ElevatedButton(text="Ask the 8-Ball", on_click=get_answer, width=200), answer],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ))

ft.app(target=main)
