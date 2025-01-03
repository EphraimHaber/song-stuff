import warnings
import flet as ft

warnings.filterwarnings("ignore", category=DeprecationWarning)


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        if counter.data is None:
            return
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
