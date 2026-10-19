import random
import time
from functools import wraps

print("**Misión Súper Secreta: El Decorador: Agente K**")
print("El Briefing")
print("Agente, su misión si decide aceptarla... \nHemos detectado una serie de <funciones> enemigas operando dentro de nuestro sistema.\nNo sabemos qué información manejan ni qué secretos producen, pero son una amenaza potencial.")

Aceptacion = input("Aceptas la mision (si/no): ").strip().lower()

if Aceptacion == "si":
    print("\nSu departamento de I+D ha desarrollado un arma de vigilancia de última generación: el decorador de infiltración `@agente_K`.\nSu trabajo es desplegar este decorador para interceptar y reportar toda la actividad de estas funciones objetivo sin que ellas se den cuenta.\n")
else: 
    print("¡Misión Fallida!")
    exit()


def desactivar_bomba(codigo="código-azul", tiempo_restante=15):
    print("\n🚨 [ALERTA DE SEGURIDAD]: ¡AMENAZA DETECTADA!")
    print(f"[PROCEDIMIENTO]: Ejecutando desactivar_bomba (Código: {codigo}, Tiempo: {tiempo_restante}s)...")
    print("[RESULTADO]: ¡Bomba neutralizada con éxito por el Agente K!\n")
    return "Bomba desactivada"


def agente_K(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        contenido_args = str(args).lower()
        contenido_kwargs = str(kwargs).lower()

        if "bomba" in contenido_args or "bomba" in contenido_kwargs:
            print(f"\n[INFORME]: ¡Agente K infiltrando al objetivo '{func.__name__}'!")
            print(f"[¡PELIGRO!]: Equipamiento SOSPECHOSO detectado: {args} {kwargs}")
            print(f"[ACCION]: ❌ Función '{func.__name__}' CANCELADA por seguridad.")

            desactivar_bomba()
            return "CANCELADO: Amenaza neutralizada"

        print(f"[INFORME]: ¡Agente K infiltrando al objetivo '{func.__name__}'!")
        print(f"[INTELIGENCIA]: Equipamiento táctico (args) detectado: {args}")
        print(f"[INTELIGENCIA]: Documentos secretos (kwargs) recuperados: {kwargs}")

        resultado = func(*args, **kwargs)

        print(f"[EXTRACCIÓN]: ¡Misión cumplida! Secreto: '{resultado}'\n")
        return resultado

    return wrapper


def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f'⏱️ [{func.__name__} tardó {fin - inicio:.4f} segundos.]\n')
        return resultado
    return wrapper


@medir_tiempo
@agente_K
def procesar_pasajero(nombre, equipaje):
    return f"Pasajero {nombre} ha abordado exitosamente con {equipaje}."

pasajeros = [
    ("Fernando", "traje, cepillo, zapatos"),
    ("Kelly", "laptop, libros, cargador"),
    ("Maricely", "ropa, zapatos, coca-cola"),
    ("Ana", "cámara, snacks, billetera"),
    ("Pedro", "bomba de tiempo, herramientas, control")
]

for nombre, equipo in pasajeros:
    procesar_pasajero(nombre, equipaje=equipo)