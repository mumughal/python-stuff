import unittest
from task1 import calculate


class TestStringMethods(unittest.TestCase):

    def test_calculate1(self):
        self.assertEqual(calculate("(5 + 8) * 3/8 +3"), 7.875)

    def test_calculate2(self):
        self.assertEqual(calculate("(15 + 18) - 89"), -56)


if __name__ == '__main__':
    unittest.main()