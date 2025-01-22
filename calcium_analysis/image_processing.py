from typing import Tuple, Dict, Any, List, Optional
import imageio.v3 as iio
from scipy import ndimage as ndi
from PIL import Image
from PIL.TiffTags import TAGS
import numpy as np
import os
import xml.etree.ElementTree as ET

def load_image(image_path: str) -> Tuple[np.ndarray, Dict[str, List[Any]]]:
    """
    Load an image and return its data and metadata.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    Tuple[np.ndarray, Dict[str, List[Any]]]: A tuple containing:
        - image data as numpy array
        - metadata dictionary with tag information
    """
    image: np.ndarray = iio.imread(uri=image_path)
    with Image.open(image_path) as img:
        info: Dict[str, List[Any]] = {TAGS[key]: img.tag[key] for key in img.tag.keys()}

    return image, info

def image_to_stack(image_fldr: str, save_fldr: str) -> None:
    """
    Assembles tif images into a single numpy array.

    Parameters:
    image_fldr (str): The path to the folder containing the tif images.
    save_fldr (str): The path to the folder where the .npy file will be saved.
    """
    image_files: List[str] = [f for f in os.listdir(image_fldr) if f.endswith('.tif')]
    image_count: int = len(image_files)
    print(f"Processing {image_count} images...")
    
    image_stack: List[np.ndarray] = []

    for j, image_file in enumerate(image_files, 1):
        image_path = os.path.join(image_fldr, image_file)
        print(f"Loading image {j} of {image_count} from {image_path}")
        
        image, info = load_image(image_path)
        
        root = ET.fromstring(info['ImageDescription'][0])
        num_images = int(root.find(".//prop[@id='number-of-planes']").get('value'))

        image_shape = (info['ImageLength'][0], info['ImageWidth'][0], num_images)
        print(f"Image has shape {image_shape}")

        image_data: np.ndarray = iio.imread(uri=image_path)
        image_stack.append(image_data)

    combined_stack: np.ndarray = np.concatenate(image_stack, axis=2)

    output_path: str = os.path.join(save_fldr, 'I.npy')
    print(f"Saving output to {output_path}")
    np.save(output_path, combined_stack)