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

# Aplicar umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Encontrar contornos externos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Crear copia
resultado = imagen.copy()

# Contador
cantidad = 0

# Analizar cada contorno
for contorno in contornos:

    # Calcular área
    area = cv2.contourArea(contorno)

    # Ignorar objetos demasiado pequeños
    if area > 500:

        cantidad += 1

        # Dibujar contorno
        cv2.drawContours(
            resultado,
            [contorno],
            -1,
            (0, 255, 0),
            2
        )

        # Obtener rectángulo
        x, y, ancho, alto = cv2.boundingRect(contorno)

        # Dibujar rectángulo
        cv2.rectangle(
            resultado,
            (x, y),
            (x + ancho, y + alto),
            (255, 0, 0),
            2
        )

        # Mostrar número del objeto
        cv2.putText(
            resultado,
            f"Objeto {cantidad}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# Mostrar resultado
cv2.imshow("Objetos identificados", resultado)

# Guardar
cv2.imwrite(
    "Ardilla.jpg",
    resultado
)

print("Objetos identificados:", cantidad)
print("Resultado guardado en resultados/ejemplo3_objetos.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar
cv2.destroyAllWindows()

print("Hecho por Sebastian Farfan NC = 0043")