import os
import numpy as np
from PIL import Image 

def load_image(image_path):
    """
    Load an image and return its data and metadata
    """
    with Image.open(image_path) as img:
        info = img._getexif()
        image_np = np.asarray(img)
    return image_np, info