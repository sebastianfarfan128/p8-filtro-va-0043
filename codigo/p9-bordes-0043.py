# Sebastian Farfan NC = 0043
import cv2

# Cargar imagen
imagen = cv2.imread("Ardilla.jpg")

# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Mostrar resultados
cv2.imshow("Ardilla original", imagen)
cv2.imshow("Ardilla binaria", binaria)
cv2.imshow("Contornos detectados", resultado)

# Guardar resultado
cv2.imwrite(
    "Ardilla.jpg",
    resultado
)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en resultados/Ardilla.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Hecho por Sebastian Farfan NC = 0043")