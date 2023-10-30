#!/usr/bin/python3

import unittest
add_integer = __import__('0-add_integer').add_integer

class TestCase(unittest.TestCase):
    def test_add_integer(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(1.0, 2.0), 3.0)
        self.assertEqual(add_integer(1, 2.0), 3.0)
        self.assertEqual(add_integer(1.0, 2), 3.0)
        self.assertEqual(add_integer(1.0, 2.0), 3.0)
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(1.0, 2), 3)
        self.assertEqual(add_integer(1, 2.0), 3.0)
        self.assertEqual(add_integer(1.0, 2.0), 3.0)
    def test_add_float(self):
        self.assertEqual(add_integer(1.0, 2.0), 3.0)
        self.assertEqual(add_integer(1, 2.0), 3.0)
        self.assertEqual(add_integer(1.0, 2), 3.0)
        self.assertEqual(add_integer(1.0, 2.0), 3.0)
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(1.0, 2), 3)
        self.assertEqual(add_integer(1, 2.0), 3.0)
        self.assertEqual(add_integer(1.0, 2.0), 3.0)
    def test_add_raises_exception(self):
        self.assertRaises(TypeError, add_integer, "bitch", 2.0)
        self.assertRaises(TypeError, add_integer, 0, "fuck")
        self.assertRaises(TypeError, add_integer, "bitch", "fuck")
        self.assertRaises(TypeError, add_integer, None)
        self.assertRaises(TypeError, add_integer, 1, None)
        self.assertRaises(TypeError, add_integer, None, 1)

if __name__ == "__main__":
    unittest.main()