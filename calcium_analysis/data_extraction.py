import numpy as np
from skimage import measure
from typing import List, Tuple

def roi_to_data(roi_file: str, image_file: str) -> Tuple[List[float], List[float]]:
    """
    Extract data from regions of interest in an image stack.

    This function loads a labeled image (from a .npy file), computes
    the mean intensity of each labeled region in each image in a stack,
    and saves the results.
    """

    # Load the labeled image and the image stack
    labels = np.load(roi_file)
    I_t = np.load(image_file)

    # Extract data from each region in each image
    data = []
    bkg = []
    for I in np.rollaxis(I_t, axis=2):
        # Get properties of labeled regions
        props = measure.regionprops(labels, intensity_image=I)
        
        # Compute the mean intensity of each region and the background
        avg = [prop.mean_intensity for prop in props]
        I_bkg = I.copy()
        for prop in props:
            I_bkg[prop.coords[:, 0], prop.coords[:, 1]] = np.nan
        bkg_intensity = np.nanmean(I_bkg)

        data.append(avg)
        bkg.append(bkg_intensity)

    # Save the results
    np.save('data.npy', data)
    np.save('bkg.npy', bkg)

    # Return the results
    return data, bkg
