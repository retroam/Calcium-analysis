import numpy as np
from skimage import filters, measure, segmentation, feature, io
from scipy import ndimage as ndi
from typing import Tuple
import os

class SegmentationError(Exception):
    """Custom exception for segmentation errors"""
    pass

def validate_sd(sd: float) -> None:
    """Validate standard deviation parameter"""
    if not isinstance(sd, (int, float)):
        raise ValueError("Standard deviation must be a number")
    if sd <= 0:
        raise ValueError("Standard deviation must be positive")

def stack_to_roi(image_path: str, sd: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Perform image segmentation on an image stack.

    Args:
        image_path: Path to the .npy file containing the image stack
        sd: Standard deviation parameter for processing

    Returns:
        Tuple containing (labels, mean_image, binary_image)

    Raises:
        SegmentationError: If segmentation fails
        ValueError: If parameters are invalid
    """
    validate_sd(sd)

    if not os.path.exists(image_path):
        raise ValueError(f"Image stack file not found: {image_path}")

    try:
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
        save_dir = os.path.dirname(image_path)
        np.save(os.path.join(save_dir, 'I_mean.npy'), I_mean)
        np.save(os.path.join(save_dir, 'I_bw2.npy'), I_bw2)
        np.save(os.path.join(save_dir, 'labels.npy'), labels)

        return labels, I_mean, I_bw2

    except Exception as e:
        raise SegmentationError(f"Segmentation failed: {str(e)}")
