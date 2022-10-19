import pytest
import unittest
from contexts import inharmonicDetect, models

class TestFilter(unittest.TestCase):
    def testStringDetect(self):
        fretboard = inharmonicDetect.simpleModel({0:0.01, 1:0.2, 2:0.05, 3:0.0006, 4:0.01, 5:0.34})
        assert inharmonicDetect.detectString(fretboard, 0.1999, 110).position == models.Position(1, 0)