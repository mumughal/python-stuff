import unittest
from task2 import last_number_by_peter


class TestStringMethods(unittest.TestCase):

    def test_last_number_by_peter1(self):
        self.assertEqual(last_number_by_peter(23245), 22999)

    def test_last_number_by_peter2(self):
        self.assertEqual(last_number_by_peter(11235888),11235888)

    def test_last_number_by_peter3(self):
        self.assertEqual(last_number_by_peter(111110),99999)

    def test_last_number_by_peter4(self):
        self.assertEqual(last_number_by_peter(33245),29999)


if __name__ == '__main__':
    unittest.main()