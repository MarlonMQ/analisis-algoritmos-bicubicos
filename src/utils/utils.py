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
