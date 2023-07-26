import unittest
import numpy as np
from calcium_analysis.data_extraction import roi_to_data

class TestRoiToData(unittest.TestCase):
    def setUp(self):
        # Create a mock labeled image and image stack
        self.labels = np.zeros((4, 4), dtype=int)
        self.labels[0:2, 0:2] = 1  # define one region
        self.image_stack = np.zeros((4, 4, 1))
        self.image_stack[0:2, 0:2, 0] = 2  # set region value to 2

        # Save mock data as .npy files
        np.save('mock_labels.npy', self.labels)
        np.save('mock_image_stack.npy', self.image_stack)

    def test_roi_to_data(self):
        # Call roi_to_data with the mock data files
        data, bkg = roi_to_data('mock_labels.npy', 'mock_image_stack.npy')

        # Assert that the returned data and background have the expected shapes and types
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertIsInstance(bkg, list)
        self.assertEqual(len(bkg), 1)

        # Assert the actual data and background values
        # Note: Adjust these expected values based on the exact expected outputs 
        # that should be calculated from your mock data
        expected_data = [[2.0]]  # The mean intensity of the region is 2
        expected_bkg = [0.0]  # The mean intensity of the background is 0
        self.assertEqual(data, expected_data)
        self.assertEqual(bkg, expected_bkg)

if __name__ == '__main__':
    unittest.main()
