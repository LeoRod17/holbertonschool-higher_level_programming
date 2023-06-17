import unittest
max_integer = __import__('6-max_integer').max_integer
"""Working with unicode with a function created by holberton school"""

class TestMaxInteger(unittest.TestCase):
    """I check different cases of errors"""

    def testNormal(self):
        """normal test of how it should work normaly"""
        self.assertTrue(max_integer([1, 2, 3, 4]))
        self.assertTrue(max_integer([1, 2, 4, 3]))

    def testTypeError(self):
        """a function that test if a type error hapens"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "4"])
            max_integer()


if __name__ == '__main__':
    unittest.main()
