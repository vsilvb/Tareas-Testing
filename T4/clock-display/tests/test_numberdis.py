from src.display_number import *
from unittest import TestCase

class TestNumberDisplay(TestCase):

    def setUp(self):
        self.number = NumberDisplay(9, 10)

    def test_increase(self):
        self.assertEqual(self.number.increase(), True)

    def test_reset(self):
        self.number.reset()
        self.assertEqual(self.number.value, 0)

    def test_str(self):
        self.assertEqual("0" + str(self.number.value), "09")

    def test_invariant(self):
        self.assertEqual(self.number.invariant(), True)

    def test_clone(self):
        self.assertEqual(self.number, self.number)
