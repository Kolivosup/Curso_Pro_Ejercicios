print("HOLA, CONFIGUREMOS TU CONTRASEÑA")
password = input("Ingresa tu contraseña: ")

errores = []

if len(password) < 8:
    errores.append("Debe tener al menos 8 caracteres.")
if not any(c.isupper() for c in password):
    errores.append("Debe contener al menos una letra mayúscula.")
if not any(c.islower() for c in password):
    errores.append("Debe contener al menos una letra minúscula.")
if not any(c.isdigit() for c in password):
    errores.append("Debe contener al menos un número.")
if not any(not c.isalnum() for c in password):
    errores.append("Debe contener al menos un carácter especial.")

if not errores:
    print("¡Contraseña válida y segura!")
else:
    print("La contraseña no cumple con los siguientes criterios:")
    for error in errores:
        print(f"- {error}")