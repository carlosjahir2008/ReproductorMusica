import os
from pathlib import Path
import flet as ft
from mutagen.mp3 import MP3
from mutagen.id3 import APIC, TPE1, ID3NoHeaderError
#from musica import obtenerMusi




MUSIC_EXT = ('.mp3')
print("por los momentos solo se aceptan " 
    +"archivos con extension " + MUSIC_EXT
    )



def obtenerMusi(path_folder:str) -> list[dict] :
    music = []
    folder_path = Path(path_folder)
    
    if not folder_path.exists():
        print(f"erro no se pudo acceder a : '{path_folder}'")
        return []
    
    if not folder_path.is_dir():
        print(f"Error la ruta :'{path_folder}' no es un directorio")
        return []
    
    print("Combrobaciones psasadas , accediendo a la carpeta")
    
    
    
    for item in folder_path.iterdir():
        if item.is_file() and item.suffix.lower() in MUSIC_EXT:
            metadatos = get_mp3_info(str(item.absolute()))
            music.append({
                'name'      :   item.name,
                'stem'      :   item.stem,
                'path'      :   str(item.absolute()),
                'extension' :   item.suffix.lower(),
                'artista'   :   metadatos['artist'],
                'cover_img' :   metadatos['cover_image_data'],
                'ext_img'   :   metadatos['cover_mime_type']
            })
            print(f"Archivo encontrado y agregado {item.name}  con extencion {item.suffix}  ")
    print(f"Se han encontadro {len(music)}  archivos de musica.")
    return music


def get_mp3_info(mp3_file_path: str) -> dict:
    
    info = {
        'artist': None,
        'cover_image_data': None,
        'cover_mime_type': None 
    }
    file_path = Path(mp3_file_path)

    if not file_path.exists() or not file_path.is_file():
        print(f"Advertencia: Archivo no encontrado o no es un archivo - {mp3_file_path}")
        return info
    
    
    
    if not file_path.suffix.lower() in MUSIC_EXT:
        print(f"Advertencia: El archivo {mp3_file_path} no esta soportado")
        return info

    try:
        audio = MP3(file_path)
        print(audio.tags.keys() , " -+-+-+-12")


        if 'TPE1' in audio.tags:
            info['artist'] = str(audio.tags['TPE1'])
            print(f"Artista encontrado para {file_path.name}: {info['artist']}")
        

        if 'APIC:' in audio.tags:
            apic_frame = audio.tags['APIC:']
            info['cover_image_data'] = apic_frame.data
            info['cover_mime_type'] = apic_frame.mime
            # print(f"Imagen de portada encontrada para {file_path.name}")
        
    except ID3NoHeaderError:
        print(f"Advertencia: El archivo {file_path.name} no tiene etiquetas ID3 (metadatos).")
    except Exception as e:
        print(f"Error al procesar el archivo {file_path.name}: {e}")
        
    print(info)
    return info


ruta_musica = "pruebas"

music_array = obtenerMusi(ruta_musica)
print("--------------------------------------------")
print(music_array)
