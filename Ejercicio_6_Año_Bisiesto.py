print("Bienvenido")
Año = int(input("Ingrese el año: "))
if (Año % 4 == 0 and not Año % 100 == 0) or (Año % 400 == 0):
    print("El año es BISIESTO")
else:
    print("El año NO ES BISIESTO")
