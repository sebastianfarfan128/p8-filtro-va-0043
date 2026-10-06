# Sebastian Farfan NC = 0043
import cv2
import os

# Obtener la ruta de la carpeta donde está este script ('codigo')
dir_script = os.path.dirname(os.path.abspath(__file__))

# Obtener la carpeta raíz del proyecto (un nivel arriba de 'codigo')
dir_raiz = os.path.abspath(os.path.join(dir_script, ".."))

# Construir la ruta correcta a la imagen en 'p9-filtro-va-0043/imagenes/Ardilla.jpg'
ruta_imagen = os.path.join(dir_raiz, "imagenes", "Ardilla.jpg")

# Cargar imagen
imagen = cv2.imread(ruta_imagen)

# Comprobar imagen
if imagen is None:
    print(f"Error: no se pudo cargar la imagen en '{ruta_imagen}'.")
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

# Crear la carpeta 'resultados' en la raíz si no existe
carpeta_resultados = os.path.join(dir_raiz, "resultados")
os.makedirs(carpeta_resultados, exist_ok=True)

# Guardar resultado dentro de la carpeta 'resultados'
ruta_salida = os.path.join(carpeta_resultados, "Ardilla.jpg")
cv2.imwrite(ruta_salida, resultado)

print("Cantidad de contornos encontrados:", len(contornos))
print(f"Resultado guardado en {ruta_salida}")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Hecho por Sebastian Farfan NC = 0043")