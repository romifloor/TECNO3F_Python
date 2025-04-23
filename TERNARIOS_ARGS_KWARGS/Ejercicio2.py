"""Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario"""

def buscar_palabra(*args):
    while True:
        try:
            palabra = input("Ingrese la palabra que desea buscar: ").strip()
            if not palabra:
                raise ValueError("Debe ingresar una palabra.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            resultado = "está en la lista" if palabra in args else "no está en la lista"
            print(f"La palabra '{palabra}' {resultado}.")
        finally:
            print("Búsqueda finalizada.\n")

        repetir = input("¿Desea buscar otra palabra? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa terminado.")
            break

entrada = input("Ingrese una lista de palabras separadas por comas: ")
lista_palabras = [palabra.strip() for palabra in entrada.split(",")]

buscar_palabra(*lista_palabras)
