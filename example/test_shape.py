import unittest

from coverage_filter import CoverageFilter

from shape import Square

class TestSquare(unittest.TestCase):
    @CoverageFilter('shape.py:__init__')
    def test_quare_constructor(self):
        self.assertEqual(2, Square(side=2).side)

        with self.assertRaises(ValueError):
            Square(side=0)
        with self.assertRaises(ValueError):
            Square(side=-1)

    @CoverageFilter('shape.py:area')
    def test_quare_area(self):
        self.assertEqual(4, Square(side=2).area)
