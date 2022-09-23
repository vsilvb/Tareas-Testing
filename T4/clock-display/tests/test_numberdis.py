from src.display_number import *
from unittest import TestCase

class TestNumberDisplay(TestCase):

    def setUp(self):
        self.number = NumberDisplay(4, 31)

    def test_reset(self):
        self.number.reset()
        self.assertEqual(self.number.value, 0)

    def test_increase1(self):
        self.number.value = 30
        self.assertEqual(self.number.increase(), True)

    def test_not_increase1(self):
        self.number.increase()
        self.assertEqual(self.number.value, 5)

    def test_increase2(self):
        self.number.value = 30
        self.number.increase()
        self.assertEqual(self.number.value, 0)

    def test_not_increase2(self):
        self.assertEqual(self.number.increase(), False)

    def test_increase_neg1(self):
        self.number.limit = -30
        self.number.value = -32
        self.number.increase()
        self.assertEqual(self.number.value, -1)

    def test_increase_neg2(self):
        self.number.limit = -30
        self.number.value = -32
        self.assertEqual(self.number.increase(), False)

    def test_str(self):
        self.assertEqual(self.number.str(), "04")
    
    def test_str_statement1(self):
        self.number.value = 11
        self.assertEqual(self.number.str(), "11")

    def test_str_statement2(self):
        self.number.value = 10
        self.assertEqual(self.number.str(), "10")

    def test_invariant1(self):
        self.assertEqual(self.number.invariant(), True)

    def test_invariant2(self):
        self.number.value = 31
        self.assertEqual(self.number.invariant(), False)

    def test_variant(self):
        self.number.value = 34
        self.assertEqual(self.number.invariant(), False)
