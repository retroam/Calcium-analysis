import numpy as np
import pytest
from calcium_analysis.image_segmentation import stack_to_roi

def test_stack_to_roi():
    # Create a mock image stack
    image_stack = np.random.rand(100, 100, 10)

    # Call stack_to_roi with the mock image stack and a standard deviation value
    labels, I_mean, I_bw2 = stack_to_roi(image_stack, 1)

    # Assert that the returned labels, mean image, and binary image have the expected shapes and types
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (100, 100)
    assert isinstance(I_mean, np.ndarray)
    assert I_mean.shape == (100, 100)
    assert isinstance(I_bw2, np.ndarray)
    assert I_bw2.shape == (100, 100)
```

