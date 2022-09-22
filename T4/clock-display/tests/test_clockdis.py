from src.clock_factory import *
from unittest import TestCase

class TestClockDisplay(TestCase):
    def setUp(self):
        self.factory = ClockFactory()

    # def test_demo(self):
    #     clock = self.factory.create("hh:mm")
    #     for i in range(100):
    #         clock.increment()
    #         print(clock.str())

    def test_invariant(self): 
        clock = self.factory.create("hh:mm")   
        clock.invariant()

