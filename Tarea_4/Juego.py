from pathlib import Path
import pandas as pd

# 1. Carga del archivo Excel
excel_path = Path(r"C:\Users\jeste\Downloads\matriz_decisiones_got.xlsx")

try:
    df_escenarios = pd.read_excel(excel_path, sheet_name="escenarios")
    df_pensamientos = pd.read_excel(excel_path, sheet_name="Personajes")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {excel_path}")
    exit()

personajes_map = {
    1: "Jon Snow",
    2: "Daenerys Targaryen",
    3: "Cersei Lannister",
    4: "Arya Stark"
}

# Metas de cada personaje
meta_personaje = {
    "Jon Snow": "Jon Snow",
    "Daenerys Targaryen": "Daenerys",
    "Cersei Lannister": "Cersei",
    "Arya Stark": "Jon"  # Arya lucha para que Jon reine
}

print("=" * 65)
print("BIENVENIDOS A LA MATRIZ DE DECISIONES - JUEGO DE TRONOS")
print("=" * 65)
print(
    "Las murallas exteriores de Desembarco del Rey se elevan imponentes bajo un cielo gris plomizo.\n"
    "Sobre la pasarela de la puerta principal, Missandei permanece encadenada...\n"
    "El destino de los Siete Reinos depende de cada decisión que tomes a continuación.\n"
)

def mostrar_menu():
    print("\n[SELECCIONA TU PERSONAJE]:")
    for key, name in personajes_map.items():
        print(f"{key}. {name}")
    print("5. Salir")

while True:
    mostrar_menu()
    try:
        opcion = int(input("\nOpción (1-5): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if opcion == 5:
        print("\nGracias por jugar. ¡Nos vemos en la próxima batalla!")
        break

    if opcion in personajes_map:
        nombre_personaje = personajes_map[opcion]
        meta = meta_personaje[nombre_personaje]
        
        # Obtener pensamiento y decisiones del personaje
        pensamiento = df_pensamientos[df_pensamientos["Personaje_Activo"] == nombre_personaje]
        escenarios_pj = df_escenarios[df_escenarios["Personaje_Activo"] == nombre_personaje]

        print(f"\n" + "=" * 60)
        print(f"HAS ASUMIDO EL ROL DE: {nombre_personaje.upper()}")
        print("=" * 60)
        
        # Mostrar pensamiento inicial
        if not pensamiento.empty:
            print(f"\n[Pensamiento de {nombre_personaje}]:")
            print(f"\"{pensamiento['Pensamiento'].iloc[0]}\"")

        # Lista para almacenar las decisiones tomadas por el usuario
        historial_decisiones = []
        
        # Iterar secuencialmente por la Decisión 1 y la Decisión 2
        numeros_decisiones = sorted(escenarios_pj["Numero_Decision"].unique())
        
        for num_dec in numeros_decisiones:
            opciones_actuales = escenarios_pj[escenarios_pj["Numero_Decision"] == num_dec].reset_index(drop=True)
            
            print(f"\n------------------------------------------------------------")
            print(f"--- ETAPA {num_dec}: ELIGE TU ACCIÓN ---")
            print(f"------------------------------------------------------------")
            
            for idx, row in opciones_actuales.iterrows():
                print(f"{idx + 1}. {row['Texto_Decision']}")

            # Capturar respuesta válida del usuario
            while True:
                try:
                    eleccion = int(input(f"\n¿Qué decisión tomas? (1-{len(opciones_actuales)}): "))
                    if 1 <= eleccion <= len(opciones_actuales):
                        break
                    else:
                        print(f"Ingresa un número entre 1 y {len(opciones_actuales)}.")
                except ValueError:
                    print("Por favor, ingresa un número entero.")

            # Guardar la opción elegida
            fila_elegida = opciones_actuales.iloc[eleccion - 1]
            historial_decisiones.append(fila_elegida)
            
            # Mostrar la consecuencia inmediata sin revelar quién reina aún
            print(f"\n[Desarrollo del escenario]:")
            print(fila_elegida["Desarrollo_Escenario"])

        # ---------------------------------------------------------
        # RESULTADO FINAL DEL CAMINO
        # ---------------------------------------------------------
        # Evaluamos la última decisión para determinar quién se corona
        ultima_decision = historial_decisiones[-1]
        quien_reina = ultima_decision["Quien_Reina"]

        print("\n" + "=" * 60)
        print("           RESOLUCIÓN FINAL DE LA GUERRA")
        print("=" * 60)
        
        print(f"👑 ¿QUIÉN SE CORONA REY/REINA?: {quien_reina.upper()}")
        
        # Verificación de si se logró el objetivo del personaje
        if quien_reina.strip().lower() in meta.lower():
            print(f"\n🎉 ¡VICTORIA! Lograste guiar las acciones de {nombre_personaje} para cumplir su objetivo final.")
        else:
            print(f"\n⚠️ EL DESTINO CAMBIÓ: Las decisiones tomadas no permitieron que {meta} alcanzara el trono.")
            
        print("\nResumen de tus elecciones:")
        for idx, dec in enumerate(historial_decisiones, 1):
            print(f"  Decisión {idx}: {dec['Texto_Decision']}")

        input("\nPresiona ENTER para regresar al menú principal...")

    else:
        print("Opción fuera de rango. Por favor, selecciona del 1 al 5.")