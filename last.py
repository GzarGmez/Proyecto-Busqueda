import openpyxl
import re

def leer_archivo_excel(nombre_archivo, criterio_busqueda):
    try:
        libro = openpyxl.load_workbook(nombre_archivo)
        hoja_activa = libro.active
        for fila in hoja_activa.iter_rows():
            for celda in fila:
                if celda.value and criterio_busqueda in str(celda.value):
                    for celda in fila:
                        print(celda.value, end="\t")
                    print()
                    break  # Salir del bucle al encontrar una celda válida
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

def validar_usuario(usuario):
    long = r'^\S{3,}$'
    if re.match(long, usuario):
        return True
    else:
        return False

def validar_contraseña(contraseña):
    long = r'^.{7,14}$'
    may = r'[A-Z]'
    minn = r'[a-z]'
    dig = r'\d'
    spchar = r'[^A-Za-z0-9\s]'

    mensajes = []

    if not re.match(long, contraseña):
        mensajes.append("Use entre 8 y 15 caracteres.")
    if not re.search(may, contraseña):
        mensajes.append("Use al menos una letra mayúscula.")
    if not re.search(minn, contraseña):
        mensajes.append("Use al menos una letra minúscula.")
    if not re.search(dig, contraseña):
        mensajes.append("Use al menos un dígito.")
    if not re.search(spchar, contraseña):
        mensajes.append("Use al menos un carácter especial.")
    if re.search(r'\s', contraseña):
        mensajes.append("No use espacios en blanco.")

    return mensajes

def obtener_usuario():
    while True:
        usuario = input("\nIngrese un nombre de usuario: ")
        if len(usuario.strip()) < 4:
            print("El nombre de usuario debe tener al menos 4 caracteres. Inténtelo de nuevo.")
        elif ' ' in usuario:
            print("El nombre de usuario no puede contener espacios. Inténtelo de nuevo.")
        else:
            return usuario

def obtener_contraseña():
    while True:
        contraseña = input("Ingrese una contraseña: ")
        if contraseña.strip() == "":
            print("La contraseña no puede estar vacía. Inténtelo de nuevo.")
        else:
            return contraseña

def main():
    while True:
        usuario = obtener_usuario()
        contraseña = obtener_contraseña()

        usuario_valido = validar_usuario(usuario)
        contraseña_valida = validar_contraseña(contraseña)

        if usuario_valido and not contraseña_valida:
            print("El nombre de usuario es válido y la contraseña es válida.")
            nombre_archivo = 'datospersonales.xlsx'
            criterio_busqueda = input("\nIngrese el criterio de búsqueda para el archivo Excel: ")
            leer_archivo_excel(nombre_archivo, criterio_busqueda)
            break
        else:
            print("Problemas con los campos:")
            if not usuario_valido:
                print("Nombre de usuario:")
                print("- El nombre de usuario debe tener al menos 4 caracteres y no contener espacios.")
            if contraseña_valida:
                print("Contraseña:")
                for mensaje in contraseña_valida:
                    print("-", mensaje)

if __name__ == "__main__":
    main()
