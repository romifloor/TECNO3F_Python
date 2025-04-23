"""Calcular el promedio de una lista de números usando args y un operador ternario."""

def calcular_promedio(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0

while True:
    try:
        entrada = input("\nIngrese números separados por espacio (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            print("\nFinalizando programa...")
            break
        
        numeros = []
        for num in entrada.split():
            numeros.append(float(num))  
        
        promedio = calcular_promedio(*numeros)
        print(f"El promedio de los números ingresados es: {promedio:.2f}")
    
    except ValueError:
        print("Error: Ingrese solo números válidos.")
    
    finally:
        if entrada.lower() != 'salir':  
            print("Intento de cálculo completado.")

