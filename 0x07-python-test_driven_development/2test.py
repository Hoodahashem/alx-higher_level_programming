import unittest
matrix_divided = __import__('2-matrix_divided').matrix_divided

class TestCase(unittest.TestCase):
    def test_matrix_divided(self):
        self.assertEqual(matrix_divided([[3, 6, 9],[12, 15, 18]], 3), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        self.assertEqual(matrix_divided([[1, 2, 3],[4, 5, 6]], 3), [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]])

if __name__ == '__main__':
    unittest.main()