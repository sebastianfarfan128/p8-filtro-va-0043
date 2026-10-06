# Sebastian Farfan NC = 0043
import cv2
import os

# Obtener la ruta de la carpeta donde está este script ('codigo')
dir_script = os.path.dirname(os.path.abspath(__file__))

# Obtener la carpeta raíz del proyecto (un nivel arriba de 'codigo')
dir_raiz = os.path.abspath(os.path.join(dir_script, ".."))

# Ruta dinámica a la imagen dentro de la carpeta 'imagenes'
ruta_imagen = os.path.join(dir_raiz, "imagenes", "Ardilla.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

# Comprobar si la imagen se cargó correctamente
if imagen is None:
    print(f"Error: no se pudo cargar la imagen en '{ruta_imagen}'.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbral binario
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

# Crear copia para dibujar
resultado = imagen.copy()

# Contador de objetos
cantidad = 0

# Analizar cada contorno
for contorno in contornos:
    # Calcular área
    area = cv2.contourArea(contorno)

    # Ignorar objetos demasiado pequeños
    if area > 500:
        cantidad += 1

        # Dibujar contorno verde
        cv2.drawContours(
            resultado,
            [contorno],
            -1,
            (0, 255, 0),
            2
        )

        # Obtener rectángulo delimitador
        x, y, ancho, alto = cv2.boundingRect(contorno)

        # Dibujar rectángulo azul
        cv2.rectangle(
            resultado,
            (x, y),
            (x + ancho, y + alto),
            (255, 0, 0),
            2
        )

        # Mostrar número del objeto en rojo
        cv2.putText(
            resultado,
            f"Objeto {cantidad}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# Crear la carpeta 'resultados' en la raíz si no existe
carpeta_resultados = os.path.join(dir_raiz, "resultados")
os.makedirs(carpeta_resultados, exist_ok=True)

# Ruta donde se guardará el resultado
ruta_salida = os.path.join(carpeta_resultados, "Ardilla.jpg")
cv2.imwrite(ruta_salida, resultado)

print("Objetos identificados:", cantidad)
print(f"Resultado guardado en {ruta_salida}")

# Mostrar las ventanas con la imagen original y el resultado
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Objetos identificados", resultado)

# Esperar a que el usuario presione una tecla
cv2.waitKey(0)

# Cerrar las ventanas
cv2.destroyAllWindows()

print("Hecho por Sebastian Farfan NC = 0043")