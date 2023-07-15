import numpy as np
import pytest
from calcium_analysis.data_extraction import roi_to_data

def test_roi_to_data():
    # Create a mock labeled image and image stack
    labels = np.random.randint(0, 2, size=(100, 100))
    image_stack = np.random.rand(100, 100, 10)

    # Call roi_to_data with the mock labeled image and image stack
    data, bkg = roi_to_data(labels, image_stack)

    # Assert that the returned data and background have the expected shapes and types
    assert isinstance(data, list)
    assert len(data) == 10
    assert isinstance(bkg, list)
    assert len(bkg) == 10

if __name__ == '__main__':
    coverage.run('pytest.main()')
