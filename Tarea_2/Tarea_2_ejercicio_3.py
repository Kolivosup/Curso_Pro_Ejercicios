print("BIENVENIDO")
numero = int(input("Ingresa un número entero no negativo: "))

if numero < 0:
    print("El número debe ser no negativo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")