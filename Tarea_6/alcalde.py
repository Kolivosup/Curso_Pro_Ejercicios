from usuario import Usuario, PAGOS_ALCALDIA, EVENTOS_GLOBALES, ENCUESTAS_GLOBALES

class Alcalde(Usuario):
    def __init__(self, nombre, email, password):
        super().__init__(nombre, email, password)
        self._rol = "Alcalde"

    def crear_nuevo_ciudadano(self, lista_usuarios):
        print("\n--- Registro Municipal de Ciudadanos (Alcaldía) ---")
        nombre = input("Nombre del ciudadano: ").strip()
        email = input("Correo electrónico: ").strip()
        password = input("Contraseña: ").strip()
        try:
            casa = int(input("Número de Casa asignada (1-9, excepto 5): "))
            if casa == 5:
                print("⚠️ La Casa 5 es la Plaza Comercial. Por favor asigna otra casa.")
                return
            if casa < 1 or casa > 9:
                print("⚠️ El número de casa debe estar entre 1 y 9.")
                return
            
            nuevo_u = Usuario(nombre, email, password, casa=casa)
            lista_usuarios.append(nuevo_u)
            print(f"✅ ¡Ciudadano '{nombre}' registrado exitosamente en la Casa {casa}!")
        except ValueError:
            print("⚠️ Número de casa no válido.")

    def consultar_recaudacion_real(self):
        print("\n--- Recaudación Real de Alquileres e Impuestos (Alcaldía) ---")
        if not PAGOS_ALCALDIA:
            print("Aún no se han recibido pagos de los vendedores.")
            return

        total_alquileres = sum(p['alquiler'] for p in PAGOS_ALCALDIA)
        total_impuestos = sum(p['impuesto'] for p in PAGOS_ALCALDIA)
        total_general = sum(p['total'] for p in PAGOS_ALCALDIA)

        print("Detalle de pagos recibidos:")
        for idx, p in enumerate(PAGOS_ALCALDIA, 1):
            print(f"  {idx}. {p['negocio']} -> Alquiler: ${p['alquiler']:.2f} + IVA: ${p['impuesto']:.2f} = Total: ${p['total']:.2f}")

        print(f"\n📊 RESUMEN GENERAL:")
        print(f" Total Alquileres Recaudados: ${total_alquileres:.2f}")
        print(f" Total Impuestos Recaudados (12%): ${total_impuestos:.2f}")
        print(f" Total Caja Alcaldía: ${total_general:.2f}")

    def gestionar_rutas_municipales(self):
        print("\n--- Gestión Municipal de Obras y Rutas ---")
        print("• Eliminada ruta Casa 2 a Casa 3")
        print("• Habilitada Ruta Turística con Puente (Casa 2 <-> Casa 4)")
        print("• Proyecto Casa 5: Venta de 19 losas surplus ($285) - Compra Casa 5 ($100) = Ganancia $185")
        print("• Financiamiento Asfaltado (20 losas = $300): $185 ganancia + $115 fondo municipal")

    def crear_evento(self):
        print("\n--- Crear Nuevo Evento Municipal ---")
        nombre_evt = input("Nombre del evento: ")
        fecha = input("Fecha estimada: ")
        if nombre_evt.strip():
            EVENTOS_GLOBALES.append({"nombre": nombre_evt.strip(), "fecha": fecha.strip()})
            print(f"✅ ¡Evento '{nombre_evt}' creado y publicado para todos los habitantes!")

    def menu_encuestas(self):
        while True:
            print("\n--- Gestión de Encuestas de Satisfacción ---")
            print("1. Crear nueva encuesta")
            print("2. Consultar encuestas y respuestas")
            print("3. Volver al menú principal")
            opc = input("Seleccione una opción: ")

            if opc == "1":
                pregunta = input("\nIngrese la pregunta de la encuesta: ")
                if pregunta.strip():
                    ENCUESTAS_GLOBALES.append({"pregunta": pregunta.strip(), "respuestas": []})
                    print("✅ Encuesta creada y disponible para usuarios y vendedores.")
            elif opc == "2":
                print("\n--- Resultados de Encuestas ---")
                if not ENCUESTAS_GLOBALES:
                    print("No hay encuestas creadas.")
                else:
                    for idx, enc in enumerate(ENCUESTAS_GLOBALES, 1):
                        print(f"\nEncuesta #{idx}: {enc['pregunta']}")
                        if not enc['respuestas']:
                            print("   (Aún no hay respuestas)")
                        else:
                            for r in enc['respuestas']:
                                print(f"   • {r['usuario']}: {r['respuesta']}")
            elif opc == "3":
                break

    def menu_alcalde(self, lista_usuarios):
        while True:
            print(f"\n=== MENÚ ALCALDE ({self.nombre}) ===")
            print("--- Funciones de Usuario ---")
            print("1. Consultar ruta por Origen y Destino")
            print("2. Consultar negocios")
            print("3. Hacer compras online")
            print("4. Ver eventos municipales")
            print("5. Responder encuestas")
            print("--- Funciones del Alcalde ---")
            print("6. Registrar nuevo ciudadano")
            print("7. Ver recaudación de pagos e impuestos")
            print("8. Gestión de rutas y obras públicas")
            print("9. Crear nuevo evento municipal")
            print("10. Gestión de Encuestas de Satisfacción")
            print("11. Cerrar sesión")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1": self.consultar_ruta_interactiva()
            elif opcion == "2": self.consultar_negocios()
            elif opcion == "3": self.hacer_compras_online()
            elif opcion == "4": self.ver_eventos()
            elif opcion == "5": self.responder_encuestas()
            elif opcion == "6": self.crear_nuevo_ciudadano(lista_usuarios)
            elif opcion == "7": self.consultar_recaudacion_real()
            elif opcion == "8": self.gestionar_rutas_municipales()
            elif opcion == "9": self.crear_evento()
            elif opcion == "10": self.menu_encuestas()
            elif opcion == "11":
                print(f"Cerrando sesión del Alcalde {self.nombre}...")
                break
            else:
                print("Opción no válida.")  