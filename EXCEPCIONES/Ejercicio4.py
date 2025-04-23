"""Escribe un programa que intente abrir un archivo que no existe. 
Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. 
Sin embargo, también intenta crear el archivo si no existe."""

def abrir_o_crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
        print("Intentando crear el archivo...")
        crear_archivo(nombre_archivo)
    else:
        print("Contenido del archivo:")
        print(contenido)
    finally:
        print("Proceso finalizado.")

def crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "w") as f:
            f.write("Este archivo se creó automáticamente.\n")
        print(f"El archivo '{nombre_archivo}' ha sido creado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear el archivo: {e}")

# Llamamos a la función principal
abrir_o_crear_archivo("archivo_inexistente.txt")
