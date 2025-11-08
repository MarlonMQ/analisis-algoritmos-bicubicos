import cv2
import numpy as np
from scipy.ndimage import zoom
from pathlib import Path

def scale_image(img: np.ndarray, factor: int, method: str) -> np.ndarray:
    """
    Escala una imagen según el método y factor de escala.

    Parameters:
        img (np.ndarray): Imagen en escala de grises.
        factor (int): Factor de ampliación (2 o 4).
        method (str): 'bicubico' o 'bspline'.

    Returns:
        np.ndarray: Imagen escalada.
    """
    if method == "bicubico":
        new_size = (img.shape[1] * factor, img.shape[0] * factor)
        return cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)

    elif method == "bspline":
        scaled = zoom(img, factor, order=3)
        return np.clip(scaled, 0, 255).astype(np.uint8)

    else:
        raise ValueError(f"Método desconocido: {method}")

