from cc import CuentaCorriente
from ca import CuentaAhorro

# Crear una cuenta corriente
cuenta_corriente = CuentaCorriente("Ricardo Darín", "12345678", "1993/01/17", 1000)
cuenta_corriente.depositar(500)
cuenta_corriente.extraer(200)
cuenta_corriente.extraer(600)  

# Crear una cuenta de ahorro
cuenta_ahorro = CuentaAhorro("Guillermo Francella", "87654321", "1990/10/20", 2000)
cuenta_ahorro.depositar(300)
cuenta_ahorro.extraer(100)
print(f"Interés generado: ${cuenta_ahorro.calcular_interes()}")