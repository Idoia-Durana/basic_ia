import numpy as np
import cv2

Ruta = r"C:\Users\idurana\Desktop\Python\Aprende_col_alf\Ruben_datos\Foto_figuras.png"
original = cv2.imread(Ruta)
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gris, (5, 5), 0)
canny = cv2.Canny(gauss, 50, 150)
contornos, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contorno in contornos:
    area = cv2.contourArea(contorno)
    perimetro = cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, 0.04 * perimetro, True)

    if len(approx) == 3:
        cv2.drawContours(original, [contorno], -1, (0, 255, 0), 2)
    elif len(approx) == 4: 
        cv2.drawContours(original, [contorno], -1, (0, 0, 255), 2)
    else: 
        cv2.drawContours(original, [contorno], -1, (255, 0, 0), 2)

cv2.imshow("contornos_clasificados", original)
cv2.waitKey(0)





