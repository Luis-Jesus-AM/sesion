import flet as ft

# DATOS CORRECTOS (constantes)
USER_CORRECTO = "admin"
CORREO_CORRECTO = "admin@gmail.com"
PASSWORD_CORRECTO = "1234"


def main(page: ft.Page):
    page.title = "Inicio de sesion"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    user = ft.TextField(
        label="User",
        hint_text="Usuario",
        prefix_icon=ft.Icons.PERSON,
        width=300
    )

    correo = ft.TextField(
        label="Correo",
        hint_text="Correo electronico",
        prefix_icon=ft.Icons.ALTERNATE_EMAIL,
        width=300
    )

    password = ft.TextField(
        label="Contraseña",
        hint_text="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=300
    )

    def iniciar_sesion(e):

        # si algún campo está vacío
        if user.value == "" or correo.value == "" or password.value == "":
            page.snack_bar = ft.SnackBar(
                ft.Text("Datos incorrectos ❌ Debes llenar todos los campos")
            )
            page.snack_bar.open = True
            page.update()
            return

        # validar datos correctos
        if (
            user.value == USER_CORRECTO
            and correo.value == CORREO_CORRECTO
            and password.value == PASSWORD_CORRECTO
        ):
            page.snack_bar = ft.SnackBar(
                ft.Text("Felicidades, has iniciado sesión 🎉")
            )
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Usuario o contraseña incorrectos ❌")
            )

        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Iniciar Sesion",
                    size=30,
                    weight=ft.FontWeight.W_500
                ),
                user,
                correo,
                password,

                ft.ElevatedButton(
                    "Iniciar Sesion",
                    bgcolor=ft.Colors.PURPLE,
                    color=ft.Colors.WHITE,
                    width=300,
                    on_click=iniciar_sesion
                ),

                ft.ElevatedButton(
                    "Registrarse",
                    bgcolor=ft.Colors.PURPLE,
                    color=ft.Colors.WHITE,
                    width=300
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.run(main)