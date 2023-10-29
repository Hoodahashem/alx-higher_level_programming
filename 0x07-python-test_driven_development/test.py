#!/usr/bin/python3
import add_integer
import unittest

class TestAddInteger(unittest.TestCase):
    def test_add_integer(self):
        self.assertEqual(add_integer.add_integer(1, 2), 3)
        self.assertEqual(add_integer.add_integer(1, -2), -1)
        self.assertEqual(add_integer.add_integer(1), 99)
        self.assertEqual(add_integer.add_integer(1000000, 10000000), 11000000)
        self.assertEqual(add_integer.add_integer(-130, -70), -200)
        self.assertEqual(add_integer.add_integer(-20, 10), -10)
        self.assertEqual(add_integer.add_integer(0, 0), 0)

if __name__ == '__main__':
    unittest.main()