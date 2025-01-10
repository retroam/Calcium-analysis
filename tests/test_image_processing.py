import unittest
import numpy as np
import os
from PIL import Image
from calcium_analysis.image_processing import load_image

class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        # Create a mock image and save it as a .tif file
        self.image_path = 'test_image.tif'
        self.test_image = Image.new('L', (50, 50))  # creates a grayscale image
        self.test_image.save(self.image_path)

    def tearDown(self):
        # Remove the test image file after test
        if os.path.exists(self.image_path):
            os.remove(self.image_path)

    def test_load_image(self):
        # Test loading a single image
        I, info = load_image(self.image_path)

        self.assertIsInstance(I, np.ndarray)
        self.assertIsInstance(info, dict)
        # Assuming the dimensions are returned as a single-item tuple, convert them to integers
        self.assertEqual(I.shape[0], int(info['ImageLength'][0]))
        self.assertEqual(I.shape[1], int(info['ImageWidth'][0]))

    def test_corrupt_image(self):
        """Test handling of corrupt image files"""
        # Create a corrupt image file
        with open('corrupt.tif', 'wb') as f:
            f.write(b'corrupt data')
        
        with self.assertRaises(ImageProcessingError):
            load_image('corrupt.tif')
        
        os.remove('corrupt.tif')

    def test_invalid_directories(self):
        """Test handling of invalid directories"""
        with self.assertRaises(ValueError):
            image_to_stack('/nonexistent/path', '/tmp')

if __name__ == '__main__':
    unittest.main()
