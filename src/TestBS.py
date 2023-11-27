import unittest
from BinarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        bs = BinarySearch()
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Test case for a target in the array
        result = bs.binary_search(arr, 7)
        self.assertEqual(result, 6)

        # Test case for a target not in the array
        result = bs.binary_search(arr, 11)
        self.assertEqual(result, -1)

        # Additional test cases can be added for better coverage
        # Test case for an empty array
        result = bs.binary_search([], 1)
        self.assertEqual(result, -1)

        # Test case for an array with one element
        result = bs.binary_search([1], 1)
        self.assertEqual(result, 0)
        
        # Test case for an array with two elements
        result = bs.binary_search([1, 2], 1)
        
        # Test case for an array with two elements
        result = bs.binary_search([1, 2], 3)
        self.assertEqual(result, -1)

    def test_binary_search2(self):
        bs = BinarySearch()
        arr = [1, 2, 3]
        result = bs.binary_search(arr, 1)

if __name__ == '__main__':
    unittest.main()
