import unittest
from unittest import main

def sum(a,b):
    return a + b

def div(a,b):
    return a/b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(div(3, 2), 1.5, "Should be 5")
    def test_sum_tuple(self):
        self.assertEqual(sum(3, 7),10 , "Should be 10")

test = unittest.main(exit=False)