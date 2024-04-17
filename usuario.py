import re

def usuario(user):
    long = r'^\S{3,}$'
    if re.match(long, user):
        return True
    else:
        return False

def get_user():
    while True:
        usuario = input("\nIngrese su nombre de usuario: ")
        if len(usuario.strip()) < 4:
            print("El nombre de usuario debe tener al menos 4 caracteres. Intentelo de nuevo.")
        elif ' ' in usuario:
            print("El nombre de usuario no puede contener espacios. Intentelo de nuevo.")
        else:
            return usuario

def password(passw):
    long = r'^.{7,14}$'
    may = r'[A-Z]'
    minn = r'[a-z]'
    dig = r'\d'
    spchar = r'[^A-Za-z0-9\s]'

    mensajes = []

    if not re.match(long, passw):
        mensajes.append("Use entre 8 y 15 caracteres.")
    if not re.search(may, passw):
        mensajes.append("Use al menos una letra mayuscula.")
    if not re.search(minn, passw):
        mensajes.append("Use al menos una letra minuscula.")
    if not re.search(dig, passw):
        mensajes.append("Use al menos un digito.")
    if not re.search(spchar, passw):
        mensajes.append("Use al menos un caracter especial.")
    if re.search(r'\s', passw):
        mensajes.append("No use espacios en blanco.")

    return mensajes

def get_password():
    while True:
        contrasena = input("Ingresa tu contraseña: ")
        if contrasena.strip() == "":
            print("La contraseña no puede estar vacia. Intentelo de nuevo.")
        else:
            return contrasena

def main():
    while True:
        usuario = get_user()
        gotpass = get_password()

        msgs_usuario = usuario(usuario)
        msgs = password(gotpass)

        if not msgs_usuario and not msgs:
            print("El nombre de usuario y la contraseña son validos.")
            #Aqui se debe implementar la logica
            break
        
        else:
            print("Problemas con los campos:")
            if msgs_usuario:
                print("Nombre de usuario:")
                for mensaje in msgs_usuario:
                    print("-", mensaje)
            if msgs:
                print("Contraseña:")
                for mensaje in msgs:
                    print("-", mensaje)

if __name__ == "__main__":
    main()

