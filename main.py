import flet as ft
from login import create_login
from principal import *
from musica import main_app_view


def main(page: ft.Page):
    #config pagina ---------------------
    page.title = "Reproductor"
    page.window.width = 500
    page.window.height = 500
    page.window.resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()
    #-----------------------------------
    
    
    
    def mostrar_musica():
        page.title = "Reproductor - Biblioteca"
        page.vertical_alignment = ft.MainAxisAlignment.START  
        page.clean()
        page.scroll = ft.ScrollMode.AUTO # Habilita el scroll 
        contenido = main_app_view(page)
        head = createheader(page,"Mi Musica")
        page.add(
            head,
            contenido
        )
        
        page.update()
    
    def mostrar_config():
        page.window.width = 500
        page.window.height = 600
        page.clean()
        config_view = createconfig(page,mostrar_principal)
        page.add(
            config_view
        )
    
    def mostrar_principal():   
        page.clean()
        principal_view = create1(page,mostrar_musica,mostrar_config)
        page.add(
            principal_view
        )
        
        
        page.update()
        
    
    def mostrar_login():
        page.window.opacity = 0.95
        
        page.clean()
        login_view = create_login(page,mostrar_principal)
        page.add(
            login_view,
        )
        page.update()
        
        
        
    mostrar_login()
    #mostrar_principal()
    #mostrar_config()
    #mostrar_musica()
    
    
    

ft.app(target=main)

