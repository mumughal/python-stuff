import unittest
from task3 import generate_y_values


class TestStringMethods(unittest.TestCase):

    def test_calculate1(self):
        self.assertEqual(generate_y_values("2 * x + 1", [1,2,3,4]), [3, 5, 7, 9])

    def test_calculate2(self):
        self.assertEqual(generate_y_values("(15 + 18) - 89", [1,2,3,4]), [-56, -56, -56, -56])


if __name__ == '__main__':
    unittest.main()