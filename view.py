import openpyxl
import tkinter as tk
from tkinter import ttk

def buscar_correos_por_dominio(nombre_archivo, dominio):
    resultados.delete(0, tk.END)  # Limpiar resultados anteriores
    try:
        libro = openpyxl.load_workbook(nombre_archivo)
        hoja_activa = libro.active
        for fila in hoja_activa.iter_rows():
            for celda in fila:
                if isinstance(celda.value, str) and dominio in celda.value:
                    resultados.insert(tk.END, f"{celda.value}\t")
    except FileNotFoundError:
        resultados.insert(tk.END, f"El archivo {nombre_archivo} no fue encontrado.")
    except Exception as e:
        resultados.insert(tk.END, f"Ocurrió un error: {str(e)}")

def buscar():
    dominio_a_buscar = dominio_entry.get()
    if dominio_a_buscar:
        buscar_correos_por_dominio(nombre_archivo, dominio_a_buscar)
    else:
        resultados.delete(0, tk.END)
        resultados.insert(tk.END, "Ingrese un dominio válido.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Buscador de Correos por Dominio")

# Widgets
etiqueta = ttk.Label(ventana, text="Ingrese el dominio a buscar:")
dominio_entry = ttk.Entry(ventana)
boton_buscar = ttk.Button(ventana, text="Buscar", command=buscar)
resultados = tk.Listbox(ventana, height=10, width=50)

# Colocar widgets en la ventana
etiqueta.grid(row=0, column=0, padx=10, pady=10)
dominio_entry.grid(row=0, column=1, padx=10, pady=10)
boton_buscar.grid(row=0, column=2, padx=10, pady=10)
resultados.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

nombre_archivo = 'Datos.xlsx'

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()