from usuario import Usuario
from vendedor import Vendedor
from alcalde import Alcalde

# --- USUARIOS DEL SISTEMA ---
USUARIOS = [
    # 8 Residentes de Casas
    Usuario("Carlos", "carlos@mail.com", "1234", casa=1),
    Usuario("Beatriz", "beatriz@mail.com", "casa2pass", casa=2),
    Usuario("Camilo", "camilo@mail.com", "casa3pass", casa=3),
    Usuario("Diana", "diana@mail.com", "casa4pass", casa=4),
    Usuario("Eduardo", "eduardo@mail.com", "casa6pass", casa=6),
    Usuario("Fernanda", "fernanda@mail.com", "casa7pass", casa=7),
    Usuario("Gabriel", "gabriel@mail.com", "casa8pass", casa=8),
    Usuario("Helena", "helena@mail.com", "casa9pass", casa=9),

    # 4 Vendedores de la Plaza Comercial (Casa 5)
    Vendedor("Ana", "abarrotes@mail.com", "abarrotes123", id_negocio=1),
    Vendedor("María", "maria@mail.com", "vendedor123", id_negocio=2),
    Vendedor("Pedro", "pizzeria@mail.com", "pizza123", id_negocio=3),
    Vendedor("Luis", "artesanias@mail.com", "arte123", id_negocio=4),

    # Alcalde
    Alcalde("Atlas", "alcalde@ciudadlodosa.gob", "admin2026")
]


def sistema_login():
    while True:
        print("\n==========================================")
        print("      SISTEMA CIUDAD LODOSA v7.0          ")
        print("==========================================")
        print("1. Iniciar sesión")
        print("2. Salir")
        opc = input("Seleccione una opción: ")
        
        if opc == "1":
            email = input("Correo electrónico: ")
            password = input("Contraseña: ")
            
            usuario_autenticado = None
            for u in USUARIOS:
                if u.verificar_credenciales(email, password):
                    usuario_autenticado = u
                    break
            
            if usuario_autenticado:
                print(f"\n¡Bienvenido/a {usuario_autenticado.nombre}!")
                
                if isinstance(usuario_autenticado, Alcalde):
                    usuario_autenticado.menu_alcalde(USUARIOS)
                else:
                    usuario_autenticado.menu()
            else:
                print("\n❌ Credenciales incorrectas.")
        elif opc == "2":
            print("¡Gracias por usar Ciudad Lodosa! Hasta luego.")
            break


if __name__ == "__main__":
    sistema_login()