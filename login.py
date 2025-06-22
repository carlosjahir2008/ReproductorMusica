import flet as ft

def create_login(page: ft.Page , exito):
    
    def login_click(e):
        user = username_I.value
        passw = password_I.value
        
        
        if user =="" or passw=="":
            status.value = "Ingrese sus datos!"
            page.update()
            return
        
        if user=="1" and passw =="1":
            status.value = f"Has iniciado sesicon como {user}"
            status.color = ft.Colors.GREEN_600
            page.update()
            exito()
        else:
            status.value = "Contraseña o usuario incorrecto."
            page.update()
    
    #Declaracion -----------------------
    label1_titulo = ft.Text("Inicia sesion o Registrate!" , size=22 , weight=ft.FontWeight.BOLD,font_family="segueui")
    label2 = ft.Text("\n\nO Registrate." , weight=ft.FontWeight.BOLD , size=14 ,font_family="segueui")
    status = ft.Text("" , weight=ft.FontWeight.BOLD ,font_family="segueui",color=ft.Colors.RED_500,size=20)

    username_I = ft.TextField(
        label="Usuario",
        hint_text="Ingrese su ususario/user",
        width=300,
        border="underline",
        
    )
    
    password_I = ft.TextField(
        label="contraseña",
        hint_text="Ingrese la contraseña",
        password=True,
        width=300,
        can_reveal_password=True,
        border="underline",
        text_align=ft.TextAlign.START,
        
    )
    
    boton_in  = ft.ElevatedButton(text="Iniciar sesion",on_click=login_click, width=300,height=50)
    boton_reg = ft.ElevatedButton(text="Registrate",on_click="", width=150,height=40)
    
    #contenido --------------------------
    
    
    return ft.Column([
            label1_titulo,
            status,
            username_I,
            password_I,
            boton_in,
            label2,
            boton_reg,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,       
        )
        
        
        
        
    


