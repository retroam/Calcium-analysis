import imageio.v3 as iio
from scipy import ndimage as ndi
from PIL import Image
from PIL.TiffTags import TAGS
import numpy as np
import os
import xml.etree.ElementTree as ET

def load_image(image_path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Load an image and return its data and metadata.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    Tuple[np.ndarray, Dict[str, Any]]: A tuple containing the image data and the metadata.
    """
    image = iio.imread(uri=image_path)
    with Image.open(image_path) as img:
        info = {TAGS[key] : img.tag[key] for key in img.tag.keys()}

    return image, info

def image_to_stack(image_fldr: str, save_fldr: str) -> None:
    """
    Assembles tif images in image_fld into a single numpy array and saves it to the save folder.

    This function will load each tif image in the image folder, concatenate them into a single numpy array,
    and save the array to a .npy file in the save folder.

    Parameters:
    image_fldr (str): The path to the folder containing the tif images.
    save_fldr (str): The path to the folder where the .npy file will be saved.

    Returns:
    None
    """
    image_files = [f for f in os.listdir(image_fldr) if f.endswith('.tif')]
    image_count = len(image_files)
    print(f"Processing {image_count} images...")
    I_t = []

    for j, image_file in enumerate(image_files, 1):
        image_path = os.path.join(image_fldr, image_file)
        print(f"Loading image {j} of {image_count} from {image_path}")
        
        I, info = load_image(image_path)
     
        root = ET.fromstring(info['ImageDescription'][0])
        num_images = root.find(".//prop[@id='number-of-planes']").get('value')

        num_images = len(info)
        image_shape = (info['ImageLength'][0], info['ImageWidth'][0], num_images)
        print(f"Image has shape {image_shape}")

        I_cum = iio.imread(uri=image_path)
       
        I_t.append(I_cum)

    I_t = np.concatenate(I_t, axis=2)

    output_path = os.path.join(save_fldr, 'I.npy')
    print(f"Saving output to {output_path}")
    np.save(output_path, I_t)