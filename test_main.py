import unittest
from main import reverse_array

class TestMain(unittest.TestCase):
    def test_reverse_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(reverse_array(arr), [5, 4, 3, 2, 1])
        arr2 = [9, 8, 7, 6]
        self.assertEqual(reverse_array(arr2), [6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()
