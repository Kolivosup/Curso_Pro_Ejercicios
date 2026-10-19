print("Bienvenid@ a tú Calculadora")
Numero1 = float(input("ingresa un numero: "))
Numero2 = float(input("ingresa otro numero: "))
Operador = input("¿Que quieres hacer (+, -, *, /): ")

if Operador == "+":
    resultado = Numero1 + Numero2
elif Operador == "-":
    resultado = Numero1 - Numero2
elif Operador == "*":
    resultado = Numero1 * Numero2
elif Operador == "/":
    resultado = Numero1 / Numero2
else:
    resultado = "Operador no válido"

print("El resultado es:", resultado)

