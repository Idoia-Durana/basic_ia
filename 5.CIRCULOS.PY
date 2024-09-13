import cv2 
import numpy as np

# Leer la imagen
Ruta = r"C:\Users\idurana\Desktop\Python\Foto1.jpg"
imagen = cv2.imread(Ruta)


# Convertir la imagen a formato HSV (matiz, saturacion,color)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir el rango de colores azules en el espacio de color HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# Filtrar solo los píxeles azules
mask_blue = cv2.inRange(imagen_hsv, lower_blue, upper_blue)

# Aplicar un desenfoque para reducir el ruido
mask_blue = cv2.GaussianBlur(mask_blue, (9, 9), 2)

# Detectar círculos utilizando la transformada de Hough para círculos
circulos = cv2.HoughCircles(
    mask_blue,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=100
)

# Dibujar los círculos detectados en la imagen original
if circulos is not None:
    circulos = np.uint16(np.around(circulos))
    for i in circulos[0, :]:
        # Dibujar el círculo en la imagen original
        cv2.circle(imagen, (i[0], i[1]), i[2], (0, 255, 0), 2)

# Mostrar la imagen original con los círculos detectados
cv2.imshow('Circulos Azules Detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
