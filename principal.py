import flet as ft

def create1(page: ft.Page , ir_music ,config):
    # crea la view del principal , dodnde se vera opciones para ir
    label1_titulo = ft.Text("Pagina Principal" , size=22 , weight=ft.FontWeight.BOLD,font_family="segueui")
    
    def musica_ir(e):
        ir_music()
    
    def config_ir(e):
        config()
    
    def salir(e):
        page.window.close()
    
    
    boton_ir = ft.ElevatedButton(text="Mi Musica",on_click=musica_ir, width=150,height=40)
    boton_config= ft.ElevatedButton(text="Configuracion",on_click=config_ir, width=150,height=40)
    boton_salir= ft.ElevatedButton(text="Salir",on_click=salir, width=150,height=40)
    
    
    page.update()
    #contenido --------------------------
    
    return ft.Column([
            label1_titulo,
            boton_ir,
            boton_config,
            boton_salir
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,       
        )
        
        



def createconfig(page: ft.Page , atras):
    

    label1_titulo = ft.Text("Configuración", size=28, weight=ft.FontWeight.BOLD, font_family="segueui")
    check1 = ft.Checkbox(label="Recordarme.", value=False)
    check2 = ft.Checkbox(label="Abrir al Iniciar la pc.", value=False)
    
    boton_crear_user = ft.Button(text="Administrar Usuarios")
    
    
    
    
    back_button = ft.ElevatedButton(text="Atrás", on_click=lambda e: atras())

    
    return ft.Column(
        [
            # Contenedor para el título
            ft.Container(
                content=label1_titulo,
                alignment=ft.alignment.top_left,
                padding=ft.padding.only(left=20, top=20) 
            ),
            
            ft.Container(height=50),

            # Opciones de configuración
            ft.Container(
                content=ft.Column(
                    [
                    check2,
                    check1,
                    
                    ],
                    alignment=ft.alignment.top_left,
                    spacing=10,
                )
                ),
            
            ft.Container(
                content=ft.Column(
                    [
                    boton_crear_user
                    
                    ],
                    alignment=ft.alignment.top_left,
                    spacing=10,
                    
                ),
                padding=ft.padding.only(top=30)
                ),
            
            
            #aqui seguir añadiendo ,as opcs
            
            ft.Container(expand=True),

            # Boton atras 
            ft.Container(
                content=back_button,
                alignment=ft.alignment.bottom_center, 
                padding=ft.padding.only(bottom=20)
            )
        ],
        # Configuración del Column principal
        horizontal_alignment=ft.CrossAxisAlignment.START, # Alinea los hijos del Column a la izquierda horizontalmente
        alignment=ft.MainAxisAlignment.START,           # Alinea los hijos del Column al inicio (arriba) verticalmente
        spacing=0, # Ajusta el espaciado entre los elementos del Column si no quieres el espaciado predeterminado
        expand=True # Haz que el Column se expanda para llenar el espacio disponible en la página
    )
    
    
    
    
    
def createheader(page: ft.Page,titulo:str="Musica"):
    
    
    h1 = ft.Text(
                    titulo,
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    font_family="segueui"
                )
    boton_config = ft.Button(
                    "⚙️", 
                )
    boton_atras = ft.Button(
        "🔙",
    )
    
    
    return ft.Row(
            controls=[
                h1,
                ft.Container(expand=True),
                boton_config,
                boton_atras
            ],
            alignment=ft.MainAxisAlignment.START, 
            vertical_alignment=ft.CrossAxisAlignment.START,
            height=60, 
            
            
        )

    

    
    
def createMusic(page: ft.Page , ir_music ,config):
    
    
    return ft.Column([
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,       
        )