import Estaciones

import Estaciones

metro = Estaciones.Estaciones()

print("=" * 45)
print(" Bienvenido a tu verificador de estaciones")
print(" Aquí puedes calcular el trayecto de tu ruta")
print("=" * 45)

# Convertimos a formato Título para que coincida con el diccionario (ej: "plaza venezuela" -> "Plaza Venezuela")
Origen = input("¿En dónde estás? ").strip().title()
Destino = input("¿A dónde vas? ").strip().title()

def obtener_lineas_de_estacion(estacion, metro):
    lineas = []
    for nombre_linea, estaciones in metro.items():
        if estacion in estaciones:
            lineas.append(nombre_linea)
    return lineas

def buscar_ruta(Origen, Destino, metro):
    cola = [[Origen]]
    visitadas = {Origen}

    while len(cola) > 0: 
        ruta_actual = cola.pop(0)
        estacion_actual = ruta_actual[-1]

        if estacion_actual == Destino:
            return ruta_actual

        for linea in metro.values():
            if estacion_actual in linea:
                vecinas = linea[estacion_actual].get("estaciones_siguientes", [])
                
                for siguiente in vecinas:
                    if siguiente not in visitadas:
                        visitadas.add(siguiente)
                        nueva_ruta = list(ruta_actual)
                        nueva_ruta.append(siguiente)
                        cola.append(nueva_ruta)
    return None

def calcular_detalles_viaje(ruta, metro):
    tiempo_total = 0
    transferencias = []

    for i in range(len(ruta) - 1):
        est_actual = ruta[i]
        est_siguiente = ruta[i+1]
        
        # Sumar el tiempo leyendo la estación directamente
        for linea in metro.values():
            if est_actual in linea:
                vecinas = linea[est_actual].get("estaciones_siguientes", [])
                if est_siguiente in vecinas:
                    tiempo_total += linea[est_actual].get("tiempo", 0)
                    break

        # Detectar si hay cambio de línea entre la estación actual y la siguiente
        lineas_actual = set(obtener_lineas_de_estacion(est_actual, metro))
        lineas_siguiente = set(obtener_lineas_de_estacion(est_siguiente, metro))
        if not lineas_actual.intersection(lineas_siguiente):
            transferencias.append(est_actual)

    return tiempo_total, transferencias

ruta = buscar_ruta(Origen, Destino, metro)

if ruta:
    tiempo, transferencias = calcular_detalles_viaje(ruta, metro)
    print("\n" + "-" * 40)
    print(" ¡Ruta encontrada!")
    print(f" Trayecto: {' -> '.join(ruta)}")
    print(f" Estaciones recorridas: {len(ruta) - 1}")
    print(f" Tiempo total estimado: {tiempo} minutos")

    if transferencias:
        print("\n CAMBIOS DE LÍNEA:")
        for t in transferencias:
            print(f"  • Debes realizar transferencia en la estación: {t}")
    else:
        print("\n Permaneces en la misma línea durante todo el recorrido.")
    print("-" * 40)
else:
    print("\nNo se encontró una ruta. Revisa que escribiste los nombres exactos de las estaciones.")