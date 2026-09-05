print("Bienvenido")
Hora = int(input("Ingresa el número de horas: "))
Minutos = int(input("Ingresa el número de Minutos: "))
Segundos = int(input("Ingresa el número de Segundos: "))

Hora_Min = (Hora * 3600)
Min_Seg = (Minutos * 60)
Total = Hora_Min + Min_Seg + Segundos

print("Tú resultado es", Total)