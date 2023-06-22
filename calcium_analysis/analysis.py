import os
from .image_processing import image_to_stack
from .data_extraction import roi_to_data
from .image_segmentation import stack_to_roi


def run_analysis(image_fld, save_fld, sd):
    image_to_stack(image_fld, save_fld)
    stack_to_roi(save_fld, sd)
    roi_to_data(save_fld)
