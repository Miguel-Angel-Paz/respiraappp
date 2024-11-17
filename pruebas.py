import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import math

def es_nan(valor):
    """Verifica si el valor es un número y si es NaN."""
    try:
        # Si es un número, verifica si es NaN
        return math.isnan(float(valor))
    except (ValueError, TypeError):
        # Si no es un número, no es NaN
        return True

def mostrar_pagina1():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Mostrar Iconos y Valores")
    
    # Crear un Canvas
    canvas_fondo = tk.Canvas(ventana, width=800, height=600)
    canvas_fondo.pack(fill="both", expand=True)

    # Lista de iconos y valores
    iconos = ["icono1.png", "icono2.png", "icono3.png", "icono4.png", "icono5.png", "icono6.png"]
    datos_climaticos = [23.0, 19.9, 27.6, 17.7, float('nan'), 347.0, 8.5]  # Los valores de la lista

    # Crear un recuadro para los iconos y valores
    x_inicial = 100
    y_inicial = 100
    espacio_x = 90
    iconos_tk = []  # Lista para almacenar los iconos cargados

    for i, valor in enumerate(datos_climaticos):
        if i >= len(iconos):
            break  # Asegura que no se intente acceder fuera de la lista de iconos

        x_pos = x_inicial + i * espacio_x
        y_pos = y_inicial

        # Cargar ícono si existe
        try:
            icono = Image.open(iconos[i])
            icono = icono.resize((40, 40))  # Tamaño uniforme para todos los íconos
            icono_tk = ImageTk.PhotoImage(icono)
            iconos_tk.append(icono_tk)  # Mantener referencia del icono

            # Dibujar el ícono en el Canvas
            canvas_fondo.create_image(x_pos, y_pos, image=icono_tk)

            # Determinar texto del valor
            if es_nan(valor):
                texto = "N/A"
            else:
                texto = f"{valor:.1f}"  # Formatear como número decimal con un decimal

            # Dibujar el texto del valor
            canvas_fondo.create_text(x_pos, y_pos + 50, text=texto, font=("Arial", 10), fill="black")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{iconos[i]}'.")
            continue

    # Mostrar la ventana
    ventana.mainloop()

# Llamar a la función para mostrar la página con los iconos y los valores
mostrar_pagina1()
