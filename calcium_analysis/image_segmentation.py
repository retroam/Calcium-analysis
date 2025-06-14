import numpy as np
from skimage import filters, measure, segmentation, feature, io
from scipy import ndimage as ndi
from typing import Tuple

def stack_to_roi(image_path: str, sd: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Perform image segmentation on an image stack.

    This function loads a numpy array from a .npy file, performs 
    thresholding and edge detection, identifies connected components,
    and saves the results.

    Parameters:
    image_path (str): The path to the .npy file containing the image stack.
    sd (float): The standard deviation used for image segmentation.

    Returns:
    Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the labeled image, the mean image, and the binary image after morphological opening.
    """

    # Load the image stack
    I_t = np.load(image_path)

    # Compute the mean image
    I_mean = np.mean(I_t, axis=2)

    # Perform thresholding
    I_bw1 = I_mean > filters.threshold_local(I_mean, block_size=15)

    # Perform morphological opening
    I_bw2 = ndi.binary_opening(I_bw1, structure=np.ones((3, 3)))

    # Identify connected components
    labels = measure.label(I_bw2)

    # Save the results
    np.save('I_mean.npy', I_mean)
    np.save('I_bw2.npy', I_bw2)
    np.save('labels.npy', labels)

    # Return the results
    return labels, I_mean, I_bw2
