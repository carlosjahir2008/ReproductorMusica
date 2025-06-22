import flet as ft
from func.Obtener import obtenerMusi 
from principal import *

musica = obtenerMusi("pruebas")


def build_music_card(song_info: dict):
    song_path = song_info.get('path', '')
    song_title = song_info.get('stem', 'Título Desconocido')
    song_artist = song_info.get('artist', 'Artista Desconocido')

    
    #head = createheader()
    # Contenido de la tarjeta: Título, Artista y Botón de Play
    row_content = ft.Row(
        
        [
            ft.Column( # Columna para el texto (Título y Artista)
                [
                    ft.Text(
                        song_title,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS
                    ),
                    ft.Text(
                        song_artist,
                        size=12,
                        color=ft.Colors.BLUE_500,
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS
                    ),
                ],
                spacing=2,
                expand=True, # para que el buton play se mueva hasta el fondo
            ),
            ft.Button( 
                "Play ▶️",
                on_click=lambda e: print(f"Reproduciendo: {song_path}") # Lógica de reproducción aquí
            ),
        ],
        alignment=ft.MainAxisAlignment.START, # Alinea los elementos al inicio (izquierda)
        vertical_alignment=ft.CrossAxisAlignment.CENTER, # Centra verticalmente los elementos en la fila
        spacing=10,
        
        #padding=10,
    )
    
    content_card = ft.Container(
        content=row_content,
        padding=10
    )
    
    

    return ft.Card(
        content=content_card,
        elevation=20, 
        margin=ft.margin.only(bottom=10) 
    )

# --- La función principal que se pasa a ft.app ---
def main_app_view(page: ft.Page):
    # Configuración de la página
    
    
    
    
    # page.title = "Mi Reproductor"
    # page.window.width = 500
    # page.window.height = 600 # Un poco más de altura para el contenido
    # page.window.resizable = False
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.START # Alineamos al inicio para un header
    # page.scroll = ft.ScrollMode.AUTO # Habilita el scroll si hay muchas canciones
    # page.update()

    
    try:
        songs_data = obtenerMusi("pruebas")
    except Exception as e:
        print(f"Error al obtener la música: {e}")
        songs_data = [] 

    #para bruebas de un solo
    #songs_data = musica 

    
    #donde se guarda el view
    
    list_of_music_cards = []
    if songs_data:
        for song_info_dict in songs_data:
            # Para cada diccionario de canción, crea una tarjeta y la añádela a la lista
            list_of_music_cards.append(build_music_card(song_info_dict))
    else:
        list_of_music_cards.append(ft.Text(
            "No se encontraron canciones en la carpeta 'pruebas'.",
            color=ft.Colors.RED_400,
            size=16
        ))

    # Crear un contenedor Column para todas las tarjetas
    # para que se apilen como blocks
    music_library_column = ft.Column(
        list_of_music_cards,
        spacing=10, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        expand=True #para que ocupe todo
    )


    #añadimos
    
    return ft.Column(
            [
                ft.Text("Biblioteca", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(), 
                music_library_column, 
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            spacing=20, 
            expand=True 
        )
    
    



#ft.app(target=main_app_view)



