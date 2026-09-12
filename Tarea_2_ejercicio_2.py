import random

opciones = ["piedra", "papel", "tijera"]

print("BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA")
print("Escribe 'piedra', 'papel' o 'tijera'.")


usuario = input("\nTu elección: ").strip().lower()

if usuario not in opciones:
    print("Opción inválida. Debes elegir entre piedra, papel o tijera.")
else:
    computadora = random.choice(opciones)
    
    print(f"\nTú elegiste: {usuario.capitalize()}")
    print(f"La computadora eligió: {computadora.capitalize()}")
    
    if usuario == computadora:
        print("\n¡Es un EMPATE!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("\n¡GANASTE! 🎉")
    else:
        print("\nGana la computadora... ¡Inténtalo de nuevo! 🤖")
