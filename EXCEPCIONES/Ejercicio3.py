"""Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
Si se produce una excepción KeyError, captura la excepción y muestra."""

def acceder_clave(diccionario, clave):
    try:
        valor = diccionario[clave]
    except KeyError:
        print('KeyError: La clave no existe en el diccionario.')
    else:
        print(f'El valor de la clave "{clave}" es: {valor}')
    finally:
        print('Operación finalizada.')

# Diccionario
mi_diccionario = {"nombre": "Pepe", "edad": 32}

# Intentar acceder a una clave que no existe
acceder_clave(mi_diccionario, "apellido")


