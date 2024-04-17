import openpyxl

def leer_archivo_excel(nombre_archivo, criterio_busqueda):
    try:
        libro = openpyxl.load_workbook(nombre_archivo)
        hoja_activa = libro.active
        for fila in hoja_activa.iter_rows():
            fila_valida = False
            for celda in fila:
                if celda.value and str(celda.value).startswith(criterio_busqueda):
                    fila_valida = True
                    break  # Salir del bucle al encontrar una celda válida
            if fila_valida:
                for celda in fila:
                    print(celda.value, end="\t")
                print()
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Reemplaza 'archivo.xlsx' con el nombre de tu archivo .xlsx
nombre_archivo = 'datospersonales.xlsx'
criterio_busqueda = input("Ingresa el criterio de búsqueda: ")  # Capturar la búsqueda del usuario
leer_archivo_excel(nombre_archivo, criterio_busqueda)

