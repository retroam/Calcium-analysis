import os
from typing import Dict, Any
from .image_processing import image_to_stack, ImageProcessingError
from .data_extraction import roi_to_data
from .image_segmentation import stack_to_roi, SegmentationError


class AnalysisError(Exception):
    """Custom exception for analysis pipeline errors"""

    pass


def run_analysis(image_fld: str, save_fld: str, sd: float) -> Dict[str, Any]:
    """
    Run the complete analysis pipeline.

    Returns:
        Dict containing analysis results and status

    Raises:
        AnalysisError: If any step of the analysis fails
    """
    try:
        # Step 1: Image to stack conversion
        stack_path = image_to_stack(image_fld, save_fld)

        # Step 2: ROI detection
        labels, mean_image, binary_image = stack_to_roi(
            os.path.join(save_fld, "I.npy"), sd
        )

        # Step 3: Data extraction
        data, background = roi_to_data(
            os.path.join(save_fld, "labels.npy"), os.path.join(save_fld, "I.npy")
        )

        return {
            "status": "success",
            "stack_path": stack_path,
            "labels": labels,
            "mean_image": mean_image,
            "binary_image": binary_image,
            "data": data,
            "background": background,
        }

    except (ImageProcessingError, SegmentationError) as e:
        raise AnalysisError(f"Analysis failed: {str(e)}")
