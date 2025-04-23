"""Calcular el mayor de dos números ingresados por teclado usando un operador ternario."""

def encontrar_mayor():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: debe ingresar valores numéricos válidos.")
        else:
            mayor = num1 if num1 > num2 else num2
            print(f"El número mayor es: {mayor}")
        finally:
            print("Cálculo finalizado.\n")

        repetir = input("¿Desea comparar otros dos números? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa terminado.")
            break

# Llamada a la función
encontrar_mayor()
