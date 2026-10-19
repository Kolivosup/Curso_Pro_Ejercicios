print("Bienvenido, Mundano")
Precio = float(input("Indicame el Precio del Producto: "))
Descuento = float(input("Ingrese su Porcentaje de Descuento: "))
Precio_del_Descuento = ((Precio * Descuento) / 100)
Precio_Total = Precio - Precio_del_Descuento
print("El monto a pagar es de ", Precio_Total)
