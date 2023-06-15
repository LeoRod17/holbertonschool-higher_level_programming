import unittest

class TestStringMethods(unittest.TestCase):
    def testNull(self):
        self.assertIsNone()
    def testInt(self):
        self.assertIsInstance(int)
        


if __name__ == '__main__':
    unittest.main()