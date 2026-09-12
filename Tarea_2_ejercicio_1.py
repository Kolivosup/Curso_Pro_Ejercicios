import random

print("BIENVENIDO - ADIVINA EL NUMERO")
numero_secreto = random.randint(1, 100)
intentos = 0

print("Estoy pensando en un número entre 1 y 100...")
while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número es MAYOR.")
    elif intento > numero_secreto:
        print("El número es MENOR.")
    else:
        print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
        break