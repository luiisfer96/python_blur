import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def cargar_imagen():
    # Abrir un cuadro de diálogo para seleccionar un archivo de imagen
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if ruta_imagen:
        # Cargar la imagen usando PIL
        imagen = Image.open(ruta_imagen)
        # Redimensionar la imagen para ajustarla a la ventana
        # relación de aspecto 3:4
        imagen = imagen.resize((450, 600), Image.LANCZOS)
        # Convertir la imagen a un objeto ImageTk
        imagen_tk = ImageTk.PhotoImage(imagen)
        # Actualizar la etiqueta para mostrar la imagen
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk
        
        # Crear y mostrar el botón para ejecutar otra función después de cargar la imagen
        boton_otra_funcion = tk.Button(ventana, text="Ejecutar otra función", command=otra_funcion)
        boton_otra_funcion.pack(pady=10)

def otra_funcion():
    print("Botón presionado. Ejecutando otra función...")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cargar y mostrar imagen")

# Crear un botón para cargar la imagen
boton_cargar = tk.Button(ventana, text="Cargar imagen", command=cargar_imagen)
boton_cargar.pack(pady=20)

# Crear una etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack()

# Ejecutar la aplicación
ventana.mainloop()
