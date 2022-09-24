from src.clock_factory import *
from unittest import TestCase

class TestClockFactory(TestCase):
    def setUp(self):
        self.factory = ClockFactory()

    # def test_demo(self):
    #      clock = self.factory.create("hh:mm")
    #      for i in range(100):
    #          clock.increment()

