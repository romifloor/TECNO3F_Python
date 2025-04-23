""" Escribe un programa que intente sumar un número y una cadena. 
Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario."""

def sumar(a, b):
    try:
        suma = a + b
    except TypeError:
        print("Error: No se puede sumar un valor tipo cadena con un número.")
    else:
        print(f"El resultado es: {suma}")
    finally:
        print("Operación finalizada.")

# Llamada a la función con una cadena y un número
sumar("hola", 10)
