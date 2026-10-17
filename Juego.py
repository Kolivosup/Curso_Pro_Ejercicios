import pandas as pd

excel_path = r"C:\Users\jeste\Downloads\matriz_decisiones_got.xlsx"

df_escenarios = pd.read_excel(excel_path, sheet_name="escenarios")
df_pensamientos = pd.read_excel(excel_path, sheet_name="Personajes")

print("BIENVENIDOS A ESTA AVENTURA")

print("Las murallas exteriores de Desembarco del Rey se elevan imponentes bajo un cielo gris plomizo cargado de tensión. \nSobre la pasarela de la puerta principal, Missandei de Naath permanece encadenada, custodiada por la silueta colosal de Ser Gregor Cleghorne. \nAbajo, el viento del mar agita los estandartes del lobo y del dragón. \nDos ejércitos masivos contienen el aliento en un silencio sepulcral, fijos en la mano levantada de la Reina Lannister. \nEl tiempo parece haberse detenido.")

print("Elige a tu personaje")

personajes_map = {
    1: "Jon Snow",
    2: "Daenerys Targaryen",
    3: "Cersei Lannister",
    4: "Arya Stark"
}

def menu(): 
    print("\n1. Jon Snow")
    print("2. Daenerys Targaryen")
    print("3. Cersei Lannister")
    print("4. Arya Stark")
    print("5. Salir")


while True:
    menu()
    try:
        personaje = int(input("Selecciona (1:5): "))
    except ValueError:
        print("Por favor, ingresa un número válido del 1 al 5.")
        continue

    if personaje == 5:
        print("Gracias por adentrarte a esta aventura, nos vemos en otra oportunidad.")
        break

    elif personaje in personajes_map:
        nombre_personaje = personajes_map[personaje]
        
        pensamiento = df_pensamientos[df_pensamientos["Personaje_Activo"] == nombre_personaje]
        decisiones = df_escenarios[df_escenarios["Personaje_Activo"] == nombre_personaje]

        print(f"\n================ HAS ELEGIDO A: {nombre_personaje.upper()} ================")
        
        if not pensamiento.empty:
            print(f"\n[Pensamiento de {nombre_personaje}]:")
            print(pensamiento["Pensamiento"].values[0])

        print(f"\n[Decisiones disponibles]:")
        for idx, row in decisiones.iterrows():
            print(f"- Decisión {row['Numero_Decision']}: {row['Texto_Decision']}")
            print(f"  Consecuencia: {row['Desarrollo_Escenario']}\n")

    else:
        print("Opción inválida. Intenta nuevamente.")