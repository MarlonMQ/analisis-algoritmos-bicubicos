import cv2
from pathlib import Path
from core.bicubib_scaling import scale_image
from utils.utils import save_image

# === Configuración general ===
input_folder = Path("data/processed/bloque_256_bn")
output_root = Path("data/scaled")
output_root.mkdir(parents=True, exist_ok=True)

scales = [2, 4]
methods = ["bicubico", "bspline"]

# === Bucle principal ===

def main():
    print("Ejecución del proyecto ITMOS-Bicúbicos")
    
    for img_file in input_folder.glob("*.jpg"):
        img = cv2.imread(str(img_file), cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"No se pudo leer {img_file}")
            continue

        for factor in scales:
            for method in methods:
                scaled_img = scale_image(img, factor, method)
                save_image(scaled_img, factor, method, img_file.name, output_root)

        print(f"Procesada: {img_file.name}")

    print("Escalado completado para todos los factores y métodos.")

if __name__ == "__main__":
    main()
