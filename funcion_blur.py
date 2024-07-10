from rembg import remove 
from PIL import Image, ImageFilter


# rutas de almacenamiento
input_path = 'foto1.png' 
output_path = 'output1.png'
sick_image_path = 'resultado1.png'

# lectura de imagen
input_image = Image.open(input_path)

# quitar el fondo
output_image = remove(input_image)

# guarda la imagen sin fondo
output_image.save(output_path)

# filtro gaussiano
blurred_image = input_image.filter(ImageFilter.GaussianBlur(6))

# sobreposición de imágenes
blurred_image.paste(output_image, (0, 0), output_image)

# resultado
blurred_image.save(sick_image_path)