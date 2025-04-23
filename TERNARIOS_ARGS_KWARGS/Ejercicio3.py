"""Determinar si un número es par o impar."""

def par_o_impar():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
        except ValueError:
            print("Error: debe ingresar un número entero válido.")
        else:
            resultado = "par" if numero % 2 == 0 else "impar"
            print(f"El número {numero} es {resultado}.")
        finally:
            print("Verificación completada.\n")

        repetir = input("¿Desea verificar otro número? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa terminado.")
            break

par_o_impar()

