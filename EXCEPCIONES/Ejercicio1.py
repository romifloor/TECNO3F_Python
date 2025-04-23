"""Escribe un programa que intente dividir dos números. 
Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario."""

def dividir_numeros():
    try:
        # Solicitamos al usuario que ingrese dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = num1 / num2

    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

    else:
        print(f"El resultado de la división es: {resultado}")

    finally:
        print("Operación finalizada.")

# Llamamos a la función
dividir_numeros()

