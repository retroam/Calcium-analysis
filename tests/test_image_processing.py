import unittest
import numpy as np
import os
from PIL import Image
from calcium_analysis.image_processing import load_image

class TestImageProcessing(unittest.TestCase):
    
    def test_load_image(self):
        # Test loading a single image
        image_path = 'path_to_a_test_image.tif'
        I, info = load_image(image_path)

        self.assertIsInstance(I, np.ndarray)
        self.assertIsInstance(info, dict)
        self.assertEqual(I.shape[0], info['ImageLength'])
        self.assertEqual(I.shape[1], info['ImageWidth'])

if __name__ == '__main__':
    unittest.main()
