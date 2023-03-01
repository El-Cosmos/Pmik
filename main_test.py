import unittest
from sorting import quickSort
from sorting import selectionSort
from sorting import insertionSort
from sorting import bubbleSort


class TestSortingFile(unittest.TestCase):

    def test_file(self):
        # test bubble sort
        self.assertEqual(bubbleSort([]), [])
        self.assertEqual(bubbleSort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubbleSort([6, 5, 4]), [4, 5, 6])
        self.assertEqual(bubbleSort([-7, -8, -9]), [-9, -8, -7])
        # selection sort
        self.assertEqual(selectionSort([]), [])
        self.assertEqual(selectionSort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(selectionSort([6, 5, 4]), [4, 5, 6])
        self.assertEqual(selectionSort([-7, -8, -9]), [-9, -8, -7])
        # insertion sort
        self.assertEqual(insertionSort([]), [])
        self.assertEqual(insertionSort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(insertionSort([6, 5, 4]), [4, 5, 6])
        self.assertEqual(insertionSort([-7, -8, -9]), [-9, -8, -7])
        # quick sort
        self.assertEqual(quickSort([]), [])
        self.assertEqual(quickSort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(quickSort([6, 5, 4]), [4, 5, 6])
        self.assertEqual(quickSort([-7, -8, -9]), [-9, -8, -7])
