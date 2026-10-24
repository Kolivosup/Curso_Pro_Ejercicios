import collections

# --- MAPA Y RUTAS ---
# Casa 5 = Plaza Comercial (No hay habitante)
MAPA_CASAS = {
    1: [(2, 2), (9, 4)],
    2: [(1, 2), (4, 3)],  # Puente Turístico entre Casa 2 y Casa 4 (3 losas)
    3: [(4, 2), (6, 3)],
    4: [(2, 3), (3, 2), (5, 2), (7, 3)],  # Conecta con la Plaza (Casa 5)
    5: [(4, 2), (6, 2), (8, 3)],  # Casa 5: Plaza Comercial
    6: [(3, 3), (5, 2), (9, 2)],
    7: [(4, 3), (8, 2)],
    8: [(5, 3), (7, 2), (9, 2)],
    9: [(1, 4), (6, 2), (8, 2)]
}

def calcular_ruta(origen, destino):
    if origen not in MAPA_CASAS or destino not in MAPA_CASAS:
        return None, 0
    
    queue = collections.deque([(origen, [origen], 0)])
    visitados = {origen: 0}
    mejor_camino = None
    menor_losas = float('inf')
    
    while queue:
        actual, camino, losas = queue.popleft()
        
        if actual == destino:
            if losas < menor_losas:
                menor_losas = losas
                mejor_camino = camino
            continue
            
        for vecino, peso in MAPA_CASAS[actual]:
            nuevo_losas = losas + peso
            if vecino not in visitados or nuevo_losas < visitados[vecino]:
                visitados[vecino] = nuevo_losas
                queue.append((vecino, camino + [vecino], nuevo_losas))
                
    return mejor_camino, menor_losas


# --- REGISTROS GLOBALES COMPARTIDOS ---
class Negocio:
    def __init__(self, id_negocio, nombre, vendedor_email):
        self.id_negocio = id_negocio
        self.nombre = nombre
        self.vendedor_email = vendedor_email
        self.pedidos = []
        self.balance_ventas = 0.0
        self.catalogo = {}

NEGOCIOS_GLOBALES = {
    1: Negocio(1, "Tienda de Abarrotes", "abarrotes@mail.com"),
    2: Negocio(2, "Cafetería del Puente", "maria@mail.com"),
    3: Negocio(3, "Pizzería La Losa", "pizzeria@mail.com"),
    4: Negocio(4, "Artesanías El Barro", "artesanias@mail.com")
}

PAGOS_ALCALDIA = []
EVENTOS_GLOBALES = [
    {"nombre": "Inauguración del Puente Turístico", "fecha": "Próximamente"},
    {"nombre": "Feria Gastronómica de la Plaza", "fecha": "Este fin de semana"}
]
ENCUESTAS_GLOBALES = []


class Usuario:
    def __init__(self, nombre, email, password, casa=None):
        self.nombre = nombre
        self.email = email
        self.__password = password
        self.casa = casa
        self._rol = "Usuario"

    def verificar_credenciales(self, email, password):
        return self.email.strip().lower() == email.strip().lower() and self.__password == password

    def consultar_ruta_interactiva(self):
        print("\n--- CONSULTAR RUTA (Origen -> Destino) ---")
        print("Casas disponibles: Casa 1 a Casa 9 (La Casa 5 es la Plaza Comercial)")
        try:
            origen = int(input("Seleccione Casa de Inicio (1-9): "))
            destino = int(input("Seleccione Casa de Destino (1-9): "))
            
            if origen == destino:
                print("⚠️ El origen y el destino son la misma casa.")
                return

            camino, total_losas = calcular_ruta(origen, destino)
            
            if camino:
                str_camino = " -> ".join([f"Casa {c}" for c in camino])
                print(f"\n🗺️  Ruta óptima encontrada:")
                print(f"📍 Trayecto: {str_camino}")
                print(f"🧱 Total de losas: {total_losas}")
                
                if (2 in camino and 4 in camino) and abs(camino.index(2) - camino.index(4)) == 1:
                    print("📸 ¡Atención! Esta ruta pasa por la Zona Turística del Puente (entre Casa 2 y Casa 4).")
            else:
                print("❌ No se encontró ruta.")
        except ValueError:
            print("⚠️ Entrada no válida.")

    def consultar_negocios(self):
        print("\n--- Negocios en la Plaza (Casa 5) ---")
        for id_n, neg in NEGOCIOS_GLOBALES.items():
            print(f"\n🏬 {id_n}. {neg.nombre}")
            if neg.catalogo:
                for prod, precio in neg.catalogo.items():
                    print(f"   • {prod}: ${precio:.2f}")
            else:
                print("   (Aún no tiene productos cargados por su vendedor)")

    def hacer_compras_online(self):
        print("\n--- Realizar Compra Online ---")
        print("Seleccione el negocio donde desea comprar:")
        for id_n, neg in NEGOCIOS_GLOBALES.items():
            print(f"{id_n}. {neg.nombre}")
            
        try:
            id_neg = int(input("\nNúmero de negocio: "))
            if id_neg in NEGOCIOS_GLOBALES:
                negocio = NEGOCIOS_GLOBALES[id_neg]
                
                if not negocio.catalogo:
                    print(f"\n⚠️ El negocio '{negocio.nombre}' no tiene inventario cargado todavía.")
                    print("💡 El vendedor debe cargar su lista de productos primero.")
                    return
                
                print(f"\n--- Menú de {negocio.nombre} ---")
                lista_prods = list(negocio.catalogo.items())
                for idx, (prod, precio) in enumerate(lista_prods, 1):
                    print(f"{idx}. {prod} - ${precio:.2f}")
                
                num_prod = int(input("\nSeleccione el número del producto a comprar: "))
                if 1 <= num_prod <= len(lista_prods):
                    producto_sel, precio_unitario = lista_prods[num_prod - 1]
                    cantidad = int(input(f"¿Cuántas unidades de '{producto_sel}' deseas comprar?: "))
                    
                    if cantidad <= 0:
                        print("⚠️ La cantidad debe ser mayor a 0.")
                        return

                    monto_total = precio_unitario * cantidad
                    
                    pedido = {
                        "cliente": self.nombre,
                        "producto": f"{producto_sel} (x{cantidad})",
                        "monto": monto_total,
                        "estado": "Pendiente"
                    }
                    negocio.pedidos.append(pedido)
                    negocio.balance_ventas += monto_total
                    
                    print(f"\n✅ ¡Compra realizada con éxito!")
                    print(f"🛒 Resumen: {producto_sel} x{cantidad}")
                    print(f"💵 Total a pagar: ${monto_total:.2f}")
                    print(f"📩 Pedido enviado a '{negocio.nombre}'.")
                else:
                    print("⚠️ Selección de producto no válida.")
            else:
                print("⚠️ Negocio no válido.")
        except ValueError:
            print("⚠️ Entrada no válida.")

    def ver_eventos(self):
        print("\n--- Eventos Municipales Publicados ---")
        if not EVENTOS_GLOBALES:
            print("No hay eventos programados en este momento.")
            return
        for idx, evt in enumerate(EVENTOS_GLOBALES, 1):
            print(f"{idx}. {evt['nombre']} (Fecha: {evt['fecha']})")

    def responder_encuestas(self):
        print("\n--- Encuestas Disponibles de la Alcaldía ---")
        if not ENCUESTAS_GLOBALES:
            print("No hay encuestas activas por responder.")
            return

        for idx, enc in enumerate(ENCUESTAS_GLOBALES, 1):
            print(f"\nEncuesta #{idx}: {enc['pregunta']}")
            ya_respondio = any(r['usuario'] == self.nombre for r in enc['respuestas'])
            if ya_respondio:
                print("   (Ya has respondido a esta encuesta)")
            else:
                resp = input("   Escribe tu respuesta (o ENTER para saltar): ")
                if resp.strip():
                    enc['respuestas'].append({"usuario": self.nombre, "respuesta": resp.strip()})
                    print("   ✅ ¡Gracias por tu respuesta!")

    def menu(self):
        while True:
            info_casa = f" - Casa {self.casa}" if self.casa else ""
            print(f"\n=== MENÚ USUARIO ({self.nombre}{info_casa}) ===")
            print("1. Consultar ruta por Origen y Destino")
            print("2. Consultar negocios y catálogos")
            print("3. Hacer compras online")
            print("4. Ver eventos municipales")
            print("5. Responder encuestas del Alcalde")
            print("6. Cerrar sesión")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1": self.consultar_ruta_interactiva()
            elif opcion == "2": self.consultar_negocios()
            elif opcion == "3": self.hacer_compras_online()
            elif opcion == "4": self.ver_eventos()
            elif opcion == "5": self.responder_encuestas()
            elif opcion == "6":
                print(f"Cerrando sesión de {self.nombre}...")
                break
            else:
                print("Opción no válida.")