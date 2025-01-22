from typing import List, Tuple, NDArray
import numpy as np
from skimage import measure

def roi_to_data(roi_file: str, image_file: str) -> Tuple[List[List[float]], List[float]]:
    """
    Extract data from regions of interest in an image stack.

    This function loads a labeled image (from a .npy file), computes
    the mean intensity of each labeled region in each image in a stack,
    and saves the results.

    Parameters:
    roi_file (str): The path to the .npy file containing the labeled image.
    image_file (str): The path to the .npy file containing the image stack.

    Returns:
    Tuple[List[List[float]], List[float]]: A tuple containing:
        - List of lists with mean intensities for each region in each image
        - List of background intensities for each image
    """
    labels: NDArray = np.load(roi_file)
    image_stack: NDArray = np.load(image_file)

    # Use list comprehension for better readability
    data: List[List[float]] = []
    background: List[float] = []
    
    for image in np.rollaxis(image_stack, axis=2):
        props = measure.regionprops(labels, intensity_image=image)
        
        # Use generator expression for better memory efficiency
        region_intensities = [prop.mean_intensity for prop in props]
        
        # Create background mask
        background_mask = image.copy()
        for prop in props:
            background_mask[prop.coords[:, 0], prop.coords[:, 1]] = np.nan
        background_intensity = float(np.nanmean(background_mask))

        data.append(region_intensities)
        background.append(background_intensity)

    # Save results
    np.save('data.npy', data)
    np.save('bkg.npy', background)

    return data, background
