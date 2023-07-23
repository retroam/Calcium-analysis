import coverage
import unittest
import numpy as np
import os
from PIL import Image
import calcium_analysis.image_processing  # assuming the module is named image_processing.py

class TestImageProcessing(unittest.TestCase):
    
    def test_load_image(self):
        # Test loading a single image
        image_path = 'path_to_a_test_image.tif'
        I, info = image_processing.load_image(image_path)

        self.assertIsInstance(I, np.ndarray)
        self.assertIsInstance(info, dict)
        self.assertEqual(I.shape[0], info['ImageLength'])
        self.assertEqual(I.shape[1], info['ImageWidth'])

if __name__ == '__main__':
    coverage.run('unittest.main()')
