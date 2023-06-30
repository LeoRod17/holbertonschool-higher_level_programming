#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Using unicode to test rectangle class"""

class TestRectangle(unittest.TestCase):
    def testValues(self):
        r1 = Rectangle(5,6,3,2,1)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r1.width, 5)
        self.assertAlmostEqual(r1.height, 6)
        self.assertAlmostEqual(r1.x, 3)
        self.assertAlmostEqual(r1.y, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0,0,-1,-2,5)
        with self.assertRaises(TypeError):
            r3 = Rectangle("A","B","C","E",6)

    def testArea(self):
        r1 = Rectangle(2,4)
        self.assertAlmostEquals(Rectangle.area(r1), 8)

    def teststr(self):
        r1 = Rectangle(2,4,5,6,7)
        self.assertAlmostEqual(Rectangle.__str__(r1), "[Rectangle] (7) 5/6 - 2/4")
    
    """def testupdate(self):
        r1 = Rectangle(2,4,5,6,7)
        self.assertAlmostEqual(r1.update(5,6,3,2,1),"[Rectangle] (5) 2/1 - 6/3")"""
    
    def testDictionary(self):
        r1 = Rectangle(2,4,5,6,7)
        self.assertAlmostEqual(Rectangle.to_dictionary(r1), {'x': 5, 'y': 6, 'id': 7, 'height': 4, 'width': 2})

if __name__ == '__main__':
    unittest.main()
