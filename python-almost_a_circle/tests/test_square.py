#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
"""Using unicode to test rectangle class"""


class TestRectangle(unittest.TestCase):
    def testValues(self):
        s1 = Square(5, 3, 2, 1)
        self.assertAlmostEqual(s1.id, 1)
        self.assertAlmostEqual(s1.size, 5)
        self.assertAlmostEqual(s1.x, 3)
        self.assertAlmostEqual(s1.y, 2)
        with self.assertRaises(ValueError):
            s2 = Square(0, -1, -2, 5)
        with self.assertRaises(TypeError):
            r3 = Square("A", "B", "C", "E", 6)

    def teststr(self):
        s1 = Square(2, 5, 6, 7)
        self.assertAlmostEqual(Square.__str__(s1),
                               "[Square] (7) 5/6 - 2")

    def testupdate(self):
        s1 = Square(2, 5, 6, 7)
        self.assertAlmostEqual(Square.__str__(s1),
                               "[Square] (7) 5/6 - 2")
        s1.update(id=5, size=6, x=2, y=1)
        self.assertAlmostEqual(Square.__str__(s1),
                               "[Square] (5) 2/1 - 6")

    def testDictionary(self):
        s1 = Square(2, 5, 6, 7)
        self.assertAlmostEqual(Square.to_dictionary(s1),
                                {'x': 5, 'y': 6, 'id': 7, 'size': 2})

if __name__ == '__main__':
    unittest.main()
