import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image


def convertir_jpg_a_pdf(ruta_jpg, ruta_pdf):
    # Crea un lienzo PDF
    c = canvas.Canvas(ruta_pdf, pagesize=letter)

    # Tamaño del lienzo PDF
    ancho_pdf, alto_pdf = letter

    # Carga la imagen JPG
    img = Image.open(ruta_jpg)

    # Escala la imagen para ajustarla al lienzo PDF
    ancho_img, alto_img = img.size
    proporcion_ancho = ancho_pdf / ancho_img
    proporcion_alto = alto_pdf / alto_img
    proporcion = min(proporcion_ancho, proporcion_alto)
    ancho_img *= proporcion
    alto_img *= proporcion

    # Agrega la imagen al lienzo PDF
    c.drawImage(ruta_jpg, 0, 0, width=ancho_img, height=alto_img)

    # Guarda el PDF
    c.save()


# Ruta de la imagen JPG
ruta_imagen_jpg = r"Coloque aqui su ruta"

# Obtener el nombre de la imagen sin la extensión
nombre_archivo_sin_extension = os.path.splitext(os.path.basename(ruta_imagen_jpg))[0]

# Ruta para el archivo PDF de salida en la misma carpeta
ruta_salida_pdf = os.path.join(os.path.dirname(ruta_imagen_jpg), nombre_archivo_sin_extension + ".pdf")

# Llama a la función para convertir la imagen a PDF
convertir_jpg_a_pdf(ruta_imagen_jpg, ruta_salida_pdf)

print(f"La imagen {ruta_imagen_jpg} ha sido convertida a PDF en {ruta_salida_pdf}")