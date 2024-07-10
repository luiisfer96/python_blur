import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
from rembg import remove

def cargar_imagen():
    global imagen_original, output_image
    # Abrir un cuadro de diálogo para seleccionar un archivo de imagen
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if ruta_imagen:
        # Cargar la imagen usando PIL
        imagen_original = Image.open(ruta_imagen)
        # Redimensionar la imagen para ajustarla a la ventana
        imagen_redimensionada = redimensionar_imagen(imagen_original, 600, 800)
        # Convertir la imagen a un objeto ImageTk
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        # Actualizar la etiqueta para mostrar la imagen
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk
        
        # Eliminar el fondo de la imagen
        output_image = remove(imagen_original, alpha_matting=1)
        output_image = redimensionar_imagen(output_image, 600, 800)
        
        # Mostrar los botones para aplicar el desenfoque gaussiano y guardar la imagen, y la barra de control de desenfoque
        boton_desenfoque.pack(pady=10)
        barra_desenfoque.pack(pady=10)
        boton_guardar.pack(pady=10)

def aplicar_desenfoque_gaussiano():
    global imagen_original, output_image, imagen_desenfocada
    # Obtener el valor de la barra deslizante
    radio = barra_desenfoque.get()
    # Aplicar el filtro gaussiano al fondo de la imagen con el radio seleccionado
    imagen_desenfocada = imagen_original.filter(ImageFilter.GaussianBlur(radius=radio))
    # Redimensionar la imagen desenfocada para ajustarla a la ventana
    imagen_desenfocada = redimensionar_imagen(imagen_desenfocada, 600, 800)
    # Superponer la imagen sin fondo sobre la imagen desenfocada
    imagen_desenfocada.paste(output_image, (0, 0), output_image)
    # Convertir la imagen desenfocada a un objeto ImageTk
    imagen_desenfocada_tk = ImageTk.PhotoImage(imagen_desenfocada)
    # Actualizar la etiqueta para mostrar la imagen desenfocada
    etiqueta_imagen.config(image=imagen_desenfocada_tk)
    etiqueta_imagen.image = imagen_desenfocada_tk

def guardar_imagen():
    # Abrir un cuadro de diálogo para guardar el archivo de imagen
    ruta_guardar = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png"), ("Archivos JPEG", "*.jpg;*.jpeg"), ("Todos los archivos", "*.*")])
    if ruta_guardar:
        # Guardar la imagen desenfocada
        imagen_desenfocada.save(ruta_guardar)

def redimensionar_imagen(imagen, max_width, max_height):
    # Obtener las dimensiones originales de la imagen
    original_width, original_height = imagen.size
    # Calcular la relación de aspecto
    aspect_ratio = original_width / original_height
    # Calcular las nuevas dimensiones manteniendo la relación de aspecto
    if original_width > original_height:
        new_width = min(original_width, max_width)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(original_height, max_height)
        new_width = int(new_height * aspect_ratio)
    # Redimensionar la imagen
    return imagen.resize((new_width, new_height), Image.LANCZOS)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cargar y mostrar imagen")
ventana.geometry("800x600")

# Crear un contenedor de desplazamiento
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame_interior = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_interior, anchor="nw")

# Crear un botón para cargar la imagen
boton_cargar = tk.Button(frame_interior, text="Cargar imagen", command=cargar_imagen)
boton_cargar.pack(pady=20)

# Crear una etiqueta para mostrar la imagen
etiqueta_imagen = tk.Label(frame_interior)
etiqueta_imagen.pack()

# Crear un botón para aplicar el desenfoque gaussiano
boton_desenfoque = tk.Button(frame_interior, text="Aplicar Desenfoque Gaussiano", command=aplicar_desenfoque_gaussiano)

# Crear una barra deslizante para controlar el nivel de desenfoque
barra_desenfoque = tk.Scale(frame_interior, from_=0, to=20, orient=tk.HORIZONTAL, label="Nivel de Desenfoque")

# Crear un botón para guardar la imagen
boton_guardar = tk.Button(frame_interior, text="Guardar imagen", command=guardar_imagen)

# Ejecutar la aplicación
ventana.mainloop()
