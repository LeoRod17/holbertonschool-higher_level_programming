#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Using unicode to test rectangle class"""


class TestRectangle(unittest.TestCase):
    def testValues(self):
        r1 = Rectangle(5, 6, 3, 2, 1)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r1.width, 5)
        self.assertAlmostEqual(r1.height, 6)
        self.assertAlmostEqual(r1.x, 3)
        self.assertAlmostEqual(r1.y, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 1, 1, 2, 5)
            r7 = Rectangle(1, 0, 3, 4, 5)
            r8 = Rectangle(5, 6, -1, 4, 2)
            r9 = Rectangle(6, 3, 4, -6, 2)
        with self.assertRaises(TypeError):
            r3 = Rectangle("A", 1, 2, 3, 6)
            r4 = Rectangle(1, "A", 2, 3, 4)
            r5 = Rectangle(1, 2, "A", 3, 4)
            r6 = Rectangle(1, 2, 3, "A", 4)

    def testArea(self):
        r1 = Rectangle(2, 4)
        self.assertAlmostEquals(Rectangle.area(r1), 8)

    def teststr(self):
        r1 = Rectangle(2, 4, 5, 6, 7)
        self.assertAlmostEqual(Rectangle.__str__(r1),
                               "[Rectangle] (7) 5/6 - 2/4")

    def testupdate(self):
        r1 = Rectangle(2, 4, 5, 6, 7)
        self.assertAlmostEqual(Rectangle.__str__(r1),
                               "[Rectangle] (7) 5/6 - 2/4")
        r1.update(id=5, width=6, height=3, x=2, y=1)
        self.assertAlmostEqual(Rectangle.__str__(r1),
                               "[Rectangle] (5) 2/1 - 6/3")
        r2 = Rectangle(2, 4, 5, 6, 7)
        self.assertAlmostEqual(Rectangle.__str__(r2),
                               "[Rectangle] (7) 5/6 - 2/4")
        r2.update(5, 6, 3, 2)
        self.assertAlmostEqual(Rectangle.__str__(r2),
                               "[Rectangle] (5) 2/6 - 6/3")


    def testDictionary(self):
        r1 = Rectangle(2, 4, 5, 6, 7)
        self.assertAlmostEqual(Rectangle.to_dictionary(r1),
                                {'x': 5, 'y': 6, 'id': 7, 'height': 4, 'width': 2})

if __name__ == '__main__':
    unittest.main()
