import cv2
import os
from pathlib import Path

# -----------------------------------------
# 
# Este algoritmo convierte las imágenes a 
# blanco y negro
#
# -----------------------------------------

# === Definir bloques y rutas ===
bloques = {
    "bloque_1080": {
        "input": Path("data/raw/bloque_1080"),
        "output": Path("data/processed/bloque_1080_bn")
    },
    "bloque_256": {
        "input": Path("data/raw/bloque_256"),
        "output": Path("data/processed/bloque_256_bn")
    }
}

# === Procesar cada bloque ===
for nombre_bloque, rutas in bloques.items():
    input_folder = rutas["input"]
    output_folder = rutas["output"]
    os.makedirs(output_folder, exist_ok=True)
    
    print(f"Procesando {nombre_bloque}...")
    
    # Recorrer todas las imágenes .jpg
    for img_file in input_folder.glob("*.jpg"):
        img = cv2.imread(str(img_file))
        if img is None:
            print(f"No se pudo leer: {img_file}")
            continue

        # Convertir a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Guardar con el mismo nombre
        output_path = output_folder / img_file.name
        cv2.imwrite(str(output_path), gray)
    
    # print(f" {nombre_bloque} procesado y guardado en {output_folder.resolve()}\n")

print("Todos los bloques fueron convertidos a blanco y negro correctamente.")
