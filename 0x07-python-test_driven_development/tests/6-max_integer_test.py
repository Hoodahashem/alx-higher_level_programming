#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_floatl(self):
        self.assertEqual(max_integer([1.25, 2.33, 3.67, 4.44]), 4.44)
    def test_intl_floatl(self):
        self.assertEqual(max_integer([1.25, 4.44, 4, 5]), 5)
    def test_only_one(self):
        self.assertEqual(max_integer([7]), 7)
    def test_max_first(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
    def test_max_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
    def test_non_string(self):
        self.assertEqual(max_integer(""), None)
    def test_many_strings(self):
        self.assertEqual(max_integer(["string1", "string2", "string3"]), "string3")


if __name__ == '__main__':
    unittest.main()
