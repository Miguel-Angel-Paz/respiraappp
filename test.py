import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

# Valores climáticos
datos_climaticos = [23.0, 19.9, 27.6, 17.7, np.nan, 347.0, 8.5]

# Ruta de los íconos (ajusta las rutas según tus archivos)
iconos = ["icono1.png", "icono2.png", "icono3.png", "icono4.png", "icono5.png", "icono6.png"]

def mostrar_pagina1():
    # Limpiar los widgets previos en la pestaña
    for widget in pagina1.winfo_children():
        widget.destroy()

    # Cargar la imagen de fondo
    ruta_imagen_fondo = "fondo1.jpg"  # Cambia por la ruta de tu imagen de fondo
    try:
        imagen_fondo = Image.open(ruta_imagen_fondo)
        imagen_fondo = imagen_fondo.resize((800, 600))  # Ajustar al tamaño de la pestaña
        fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen de fondo en '{ruta_imagen_fondo}'.")
        return

    # Crear un Canvas para mostrar el fondo
    canvas_fondo = tk.Canvas(pagina1, width=800, height=600)
    canvas_fondo.pack(fill="both", expand=True)

    # Colocar la imagen en el Canvas
    canvas_fondo.create_image(0, 0, anchor="nw", image=fondo_tk)

    # Almacenar la referencia de la imagen para evitar que sea recolectada por el recolector de basura
    mostrar_pagina1.fondo_tk = fondo_tk

    # Crear un gráfico para los datos climáticos
    def crear_grafico():
        # Filtrar valores válidos
        valores_validos = [valor for valor in datos_climaticos if not np.isnan(valor)]

        # Escalar valores al ancho del Canvas
        max_valor = max(valores_validos)
        min_valor = min(valores_validos)
        ancho_canvas = 700
        altura_canvas = 150

        x_offset = 50
        espacio_entre_iconos = ancho_canvas / len(valores_validos)

        iconos_tk = []
        for i, valor in enumerate(valores_validos):
            # Calcular posición X
            x = x_offset + i * espacio_entre_iconos

            # Calcular posición Y
            y = 550 - ((valor - min_valor) / (max_valor - min_valor)) * altura_canvas

            # Cargar ícono
            try:
                imagen = Image.open(iconos[i % len(iconos)])
                imagen = imagen.resize((50, 50))  # ANTIALIAS eliminado
                imagen_tk = ImageTk.PhotoImage(imagen)
                iconos_tk.append(imagen_tk)

                # Colocar ícono en el Canvas
                canvas_fondo.create_image(x, y, anchor="center", image=imagen_tk)
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo '{iconos[i % len(iconos)]}'.")

            # Agregar etiqueta con el valor
            canvas_fondo.create_text(x, y + 35, text=f"{valor:.1f}", font=("Arial", 10), fill="black")

        # Guardar referencias para evitar recolección de basura
        mostrar_pagina1.iconos_tk = iconos_tk

    # Crear el gráfico
    crear_grafico()

# Crear ventana principal
root = tk.Tk()
root.title("Interfaz con Gráfico")
root.geometry("800x600")

# Crear Notebook para pestañas
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Crear pestaña
pagina1 = ttk.Frame(notebook)
notebook.add(pagina1, text="Página 1")

# Mostrar contenido de la página
mostrar_pagina1()

# Ejecutar aplicación
root.mainloop()
