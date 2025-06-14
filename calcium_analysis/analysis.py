from .image_processing import image_to_stack
from .data_extraction import roi_to_data
from .image_segmentation import stack_to_roi


def run_analysis(image_fld: str, save_fld: str, sd: float) -> None:
    """
    Run the analysis pipeline on the given image folder.

    This function will convert the images in the image folder to a stack,
    segment the stack into regions of interest (ROIs) based on the standard deviation,
    and extract data from the ROIs.

    Parameters:
    image_fld (str): The path to the folder containing the images to be analyzed.
    save_fld (str): The path to the folder where the results will be saved.
    sd (float): The standard deviation used for image segmentation.

    Returns:
    None
    """
    image_to_stack(image_fld, save_fld)
    stack_to_roi(save_fld, sd)
    roi_to_data(save_fld)
