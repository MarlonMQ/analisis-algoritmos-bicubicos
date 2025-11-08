from pathlib import Path
import numpy as np
import cv2

def save_image(image: np.ndarray, factor: int, method: str, filename: str, output_root: Path):
    """
    Guarda una imagen escalada en la carpeta correspondiente.

    Parameters:
        image (np.ndarray): Imagen procesada.
        factor (int): Factor de escala.
        method (str): Nombre del método.
        filename (str): Nombre del archivo original.
        output_root (Path): Carpeta raíz de salida.
    """
    output_folder = output_root / f"{method}_x{factor}"
    output_folder.mkdir(parents=True, exist_ok=True)
    output_path = output_folder / filename
    cv2.imwrite(str(output_path), image)

def convert_to_grayscale(image_path: Path, output_folder: Path) -> Path:
    """
    Convierte una imagen a escala de grises y la guarda en la carpeta destino.

    Parameters:
        image_path (Path): Ruta de la imagen original.
        output_folder (Path): Carpeta donde se guardará la versión en B/N.

    Returns:
        Path: Ruta del archivo convertido.
    """
    output_folder.mkdir(parents=True, exist_ok=True)
    img = cv2.imread(str(image_path))
    if img is None:
        raise ValueError(f"No se pudo leer la imagen: {image_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_path = output_folder / image_path.name
    cv2.imwrite(str(output_path), gray)

    return output_path

def convert_folder_to_grayscale(input_folder: Path, output_folder: Path):
    """
    Convierte todas las imágenes de una carpeta a escala de grises.

    Parameters:
        input_folder (Path): Carpeta de entrada con imágenes originales.
        output_folder (Path): Carpeta destino para las imágenes en B/N.
    """
    output_folder.mkdir(parents=True, exist_ok=True)
    for img_file in input_folder.glob("*.jpg"):
        try:
            convert_to_grayscale(img_file, output_folder)
        except Exception as e:
            print(f"Error con {img_file}: {e}")
    print(f"Conversión completada en {output_folder}")