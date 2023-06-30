#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Using unicode to test base class"""


class TestBase(unittest.TestCase):
    """I check different cases of errors"""
    def test_Id(self):
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base(-5)
        self.assertAlmostEqual(b3.id, -5)
        b4 = Base(1000000)
        self.assertAlmostEqual(b4.id, 1000000)

    def functionTestToJason_Strings(self):
        self.assertAlmostEqual(Base.to_json_string(None),"[]")
        self.assertAlmostEqual(Base.to_json_string([{"id": 6}]),'[{"id": 6}]')
        self.assertAlmostEqual(Base.to_json_string([]),"[]")

    def functionTestSaveLoadToJason(self):
        Rectangle.save_to_file(None)
        self.assertAlmostEqual(Rectangle.load_from_file(), [])
        r1 = Rectangle(10,8,4,3,2)
        self.assertAlmostEqual(Square.save_to_file(r1))
        self.assertAlmostEqual(Rectangle.load_from_file("Rectangle"))
    if __name__ == '__main__':
        unittest.main()