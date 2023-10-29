import unittest
matrix_divided = __import__('2-matrix_divided').matrix_divided

class TestCase(unittest.TestCase):
    def test_matrix_divided(self):
        self.assertEqual(matrix_divided([[3, 6, 9],[12, 15, 18]], 3), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        self.assertEqual(matrix_divided([[1, 2, 3],[4, 5, 6]], 3), [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]])
        self.assertEqual(matrix_divided([[1.1, -2.2, 3.3],[4.4, 5.5, -6.6]], 3), [[0.37, -0.73, 1.1], [1.47, 1.83, -2.2]])
        self.assertEqual(matrix_divided([[1, -2.2, 3, 4.4, 5],[-6.6, 7.00, 8, 9.999, 10]], 3), [[0.33, -0.73, 1.0, 1.47, 1.67], [-2.2, 2.33, 2.67, 3.33, 3.33]])
        
    def test_matrix_divided_raises_exception(self):
        self.assertRaises(TypeError,matrix_divided,"not a list", 3)
        self.assertRaises(TypeError,matrix_divided, [[1, 2, 3],[4, 5, 6]], "not a num")
        self.assertRaises(TypeError,matrix_divided, [[1, 2, 3],[4, 5, 6]], None)
        self.assertRaises(TypeError,matrix_divided, None, 5)
        self.assertRaises(TypeError,matrix_divided, [], 5)
        self.assertRaises(TypeError,matrix_divided, [[]], 4)
        self.assertRaises(TypeError,matrix_divided,[1, 2, 3], 7)
        self.assertRaises(TypeError,matrix_divided, [[1, 2, 3],[4, "not a num", 6]],3)
        self.assertRaises(TypeError,matrix_divided, [[1, 2, 3, 4],[5, 6, 7]], 8)
        self.assertRaises(TypeError,matrix_divided, [[1, 2, 3],[5, 6, 7]], "not a num")
        self.assertRaises(ZeroDivisionError,matrix_divided, [[1, 2, 3],[5, 6, 7]], 0)

if __name__ == '__main__':
    unittest.main()