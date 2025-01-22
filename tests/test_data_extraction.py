import unittest
import numpy as np
from typing import List, Tuple
from calcium_analysis.data_extraction import roi_to_data

class TestRoiToData(unittest.TestCase):
    def setUp(self) -> None:
        self.labels: np.ndarray = np.zeros((4, 4), dtype=int)
        self.labels[0:2, 0:2] = 1
        self.image_stack: np.ndarray = np.zeros((4, 4, 1))
        self.image_stack[0:2, 0:2, 0] = 2

        np.save('mock_labels.npy', self.labels)
        np.save('mock_image_stack.npy', self.image_stack)

    def test_roi_to_data(self) -> None:
        data, bkg = roi_to_data('mock_labels.npy', 'mock_image_stack.npy')

        self.assertIsInstance(data, list)
        self.assertIsInstance(bkg, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(len(bkg), 1)

        expected_data: List[List[float]] = [[2.0]]
        expected_bkg: List[float] = [0.0]
        self.assertEqual(data, expected_data)
        self.assertEqual(bkg, expected_bkg)
