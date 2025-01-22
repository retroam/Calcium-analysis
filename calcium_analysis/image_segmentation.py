from typing import Tuple, NDArray
import numpy as np
from skimage import filters, measure
from scipy import ndimage as ndi

def stack_to_roi(image_path: str, sd: float) -> Tuple[NDArray, NDArray, NDArray]:
    """
    Perform image segmentation on an image stack.

    Parameters:
    image_path (str): The path to the .npy file containing the image stack.
    sd (float): The standard deviation used for image segmentation.

    Returns:
    Tuple[NDArray, NDArray, NDArray]: A tuple containing:
        - labeled_image: Connected components labeled image
        - mean_image: Average intensity across time
        - binary_image: Thresholded and morphologically opened image
    """
    # Load the image stack
    image_stack: NDArray = np.load(image_path)

    # Compute the mean image
    mean_image: NDArray = np.mean(image_stack, axis=2)

    # Perform thresholding
    binary_image: NDArray = mean_image > filters.threshold_local(mean_image, block_size=15)

    # Perform morphological opening
    opened_image: NDArray = ndi.binary_opening(binary_image, structure=np.ones((3, 3)))

    # Identify connected components
    labeled_image: NDArray = measure.label(opened_image)

    # Save the results
    np.save('I_mean.npy', mean_image)
    np.save('I_bw2.npy', opened_image)
    np.save('labels.npy', labeled_image)

    return labeled_image, mean_image, opened_image
