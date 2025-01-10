import imageio.v3 as iio
from scipy import ndimage as ndi
from PIL import Image
from PIL.TiffTags import TAGS
import numpy as np
import os
import xml.etree.ElementTree as ET
from typing import Tuple, Dict, Any

class ImageProcessingError(Exception):
    """Custom exception for image processing errors"""
    pass

def validate_directories(image_fldr: str, save_fldr: str) -> None:
    """Validate input and output directory paths"""
    if not os.path.exists(image_fldr):
        raise ValueError(f"Image directory does not exist: {image_fldr}")
    if not os.path.exists(save_fldr):
        os.makedirs(save_fldr)

def load_image(image_path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Load an image and return its data and metadata
    
    Raises:
        ImageProcessingError: If image cannot be loaded or is corrupt
    """
    try:
        image = iio.imread(uri=image_path)
        with Image.open(image_path) as img:
            info = {TAGS[key] : img.tag[key] for key in img.tag.keys()}
        return image, info
    except Exception as e:
        raise ImageProcessingError(f"Failed to load image {image_path}: {str(e)}")

def image_to_stack(image_fldr: str, save_fldr: str) -> str:
    """
    Assembles tif images in image_fld into a single numpy array.
    
    Returns:
        str: Path to the saved numpy array
    """
    validate_directories(image_fldr, save_fldr)
    
    image_files = [f for f in os.listdir(image_fldr) if f.endswith('.tif')]
    if not image_files:
        raise ValueError(f"No .tif files found in {image_fldr}")
    
    image_count = len(image_files)
    print(f"Processing {image_count} images...")
    I_t = []

    for j, image_file in enumerate(image_files, 1):
        image_path = os.path.join(image_fldr, image_file)
        print(f"Loading image {j} of {image_count} from {image_path}")
        
        try:
            I, info = load_image(image_path)
            
            # Get number of images from XML metadata
            root = ET.fromstring(info['ImageDescription'][0])
            num_images = int(root.find(".//prop[@id='number-of-planes']").get('value'))
            
            image_shape = (info['ImageLength'][0], info['ImageWidth'][0], num_images)
            print(f"Image has shape {image_shape}")

            I_cum = iio.imread(uri=image_path)
            I_t.append(I_cum)
            
        except (ImageProcessingError, ET.ParseError) as e:
            print(f"Warning: Skipping corrupted image {image_file}: {str(e)}")
            continue

    if not I_t:
        raise ImageProcessingError("No valid images were processed")

    I_t = np.concatenate(I_t, axis=2)
    output_path = os.path.join(save_fldr, 'I.npy')
    print(f"Saving output to {output_path}")
    np.save(output_path, I_t)
    return output_path = os.path.join(save_fldr, 'I.npy')
    print(f"Saving output to {output_path}")
    np.save(output_path, I_t)