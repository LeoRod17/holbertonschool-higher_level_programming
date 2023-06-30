#!/usr/bin/python3
"""Using unicode to test base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


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
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([{"id": 6}]), '[{"id": 6}]')
        self.assertAlmostEqual(Base.to_json_string([]), "[]")

    def functionTestSaveToFile(self):
        Base.save_to_file(None)
        self.assertAlmostEqual(os.path.exists("BaseJson"), True)

    def functionJasonString(self):
        self.assertAlmostEqual(Base.from_json_string(None), [])
        self.assertAlmostEqual(
            Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertAlmostEqual(Base.from_json_string("[]"), [])

    def test_c(self):
        dictionary = {"id": 1}
        r1 = Rectangle.create(**dictionary)
        self.assertAlmostEqual(r1.id, 1)

    if __name__ == '__main__':
        unittest.main()
