import csv
import os
from usuario import Usuario, NEGOCIOS_GLOBALES, PAGOS_ALCALDIA

class Vendedor(Usuario):
    def __init__(self, nombre, email, password, id_negocio):
        super().__init__(nombre, email, password)
        self._rol = "Vendedor"
        self.id_negocio = id_negocio
        self.negocio = NEGOCIOS_GLOBALES.get(id_negocio)

    def cargar_inventario_csv(self):
        print(f"\n--- Cargar Productos desde Archivo CSV/Excel ({self.negocio.nombre}) ---")
        print("💡 Consejo: Puedes escribir el nombre (ej: productos.csv) o arrastrar el archivo hasta esta consola.")
        
        entrada = input("\nIngrese la ruta o arrastre el archivo CSV aquí: ").strip()
        # Limpiar comillas si se arrastró el archivo en Windows/VS Code
        nombre_archivo = entrada.replace('"', '').replace("'", '')
        
        ruta_final = nombre_archivo
        if not os.path.exists(ruta_final):
            directorio_script = os.path.dirname(os.path.abspath(__file__))
            ruta_alternativa = os.path.join(directorio_script, nombre_archivo)
            if os.path.exists(ruta_alternativa):
                ruta_final = ruta_alternativa

        if not os.path.exists(ruta_final):
            print(f"❌ El archivo '{nombre_archivo}' no fue encontrado.")
            print("💡 Verifica que el archivo esté guardado como 'CSV (delimitado por comas)' en Excel.")
            return

        try:
            nuevos_productos = {}
            with open(ruta_final, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for linea in reader:
                    if linea and len(linea) >= 2:
                        prod = linea[0].strip()
                        precio = float(linea[1].strip().replace(',', '.'))
                        nuevos_productos[prod] = precio

            if nuevos_productos:
                self.negocio.catalogo.clear()  
                self.negocio.catalogo.update(nuevos_productos)
                print(f"\n✅ ¡Inventario de {self.negocio.nombre} cargado exitosamente!")
                print("Catálogo actual disponible:")
                for p, pr in self.negocio.catalogo.items():
                    print(f"  • {p}: ${pr:.2f}")
            else:
                print("⚠️ No se encontraron filas de productos válidas en el archivo.")

        except Exception as e:
            print(f"❌ Error al procesar el archivo CSV: {e}")

    def gestionar_pedidos_online(self):
        print(f"\n--- Gestión de Pedidos Online ({self.negocio.nombre}) ---")
        if not self.negocio.pedidos:
            print("No tienes pedidos registrados en este momento.")
            return

        for idx, ped in enumerate(self.negocio.pedidos, 1):
            print(f"{idx}. Cliente: {ped['cliente']} | Producto: {ped['producto']} | Monto: ${ped['monto']:.2f} | Estado: {ped['estado']}")
        
        opc = input("\nIngrese el número de pedido para marcar como 'Completado' (o ENTER para volver): ")
        if opc.isdigit():
            idx_ped = int(opc) - 1
            if 0 <= idx_ped < len(self.negocio.pedidos):
                self.negocio.pedidos[idx_ped]['estado'] = "Completado"
                print(f"✅ Pedido #{opc} completado.")

    def pagar_alquiler_e_impuestos(self, alquiler=40.0, porcentaje_impuesto=0.12):
        impuesto = alquiler * porcentaje_impuesto
        total_a_pagar = alquiler + impuesto
        
        print(f"\n--- Pago de Alquiler e Impuestos ({self.negocio.nombre}) ---")
        print(f"💰 Balance disponible en ventas: ${self.negocio.balance_ventas:.2f}")
        print(f"📋 Alquiler Base: ${alquiler:.2f}")
        print(f"📋 IVA (12%): ${impuesto:.2f}")
        print(f"💵 Total requerido a pagar: ${total_a_pagar:.2f}")
        
        if self.negocio.balance_ventas < total_a_pagar:
            print("\n❌ Saldo insuficiente. No tienes ventas suficientes registradas para cubrir el alquiler e impuestos.")
            print("💡 Consejo: Los usuarios deben realizar compras en tu negocio para aumentar tu balance.")
            return

        confirmar = input("\n¿Desea procesar el pago ahora? (s/n): ")
        if confirmar.lower() == 's':
            self.negocio.balance_ventas -= total_a_pagar
            PAGOS_ALCALDIA.append({
                "negocio": self.negocio.nombre,
                "alquiler": alquiler,
                "impuesto": impuesto,
                "total": total_a_pagar
            })
            print(f"✅ Pago de ${total_a_pagar:.2f} realizado con éxito. Nuevo balance disponible: ${self.negocio.balance_ventas:.2f}")

    def ver_balance_privado(self):
        print(f"\n--- Balance Privado ({self.negocio.nombre}) ---")
        print(f"Ventas / Saldo disponible: ${self.negocio.balance_ventas:.2f}")
        print(f"Pedidos recibidos: {len(self.negocio.pedidos)}")
        print("\nCatálogo de Productos Cargados:")
        if not self.negocio.catalogo:
            print("  (Aún no has cargado inventario)")
        else:
            for p, pr in self.negocio.catalogo.items():
                print(f"  • {p}: ${pr:.2f}")

    def menu(self):
        while True:
            print(f"\n=== MENÚ VENDEDOR ({self.nombre} - {self.negocio.nombre}) ===")
            print("--- Funciones de Usuario ---")
            print("1. Consultar ruta por Origen y Destino")
            print("2. Consultar negocios")
            print("3. Hacer compras online")
            print("4. Ver eventos municipales")
            print("5. Responder encuestas del Alcalde")
            print("--- Funciones de Vendedor ---")
            print("6. Cargar inventario desde archivo CSV/Excel")
            print("7. Ver pedidos online recibidos")
            print("8. Pagar alquiler e impuestos")
            print("9. Ver balance privado y productos")
            print("10. Cerrar sesión")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1": self.consultar_ruta_interactiva()
            elif opcion == "2": self.consultar_negocios()
            elif opcion == "3": self.hacer_compras_online()
            elif opcion == "4": self.ver_eventos()
            elif opcion == "5": self.responder_encuestas()
            elif opcion == "6": self.cargar_inventario_csv()
            elif opcion == "7": self.gestionar_pedidos_online()
            elif opcion == "8": self.pagar_alquiler_e_impuestos()
            elif opcion == "9": self.ver_balance_privado()
            elif opcion == "10":
                print(f"Cerrando sesión de {self.nombre}...")
                break
            else:
                print("Opción no válida.")