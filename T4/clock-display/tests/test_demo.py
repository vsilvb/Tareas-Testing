from src.clock_factory import *
from unittest import TestCase

class TestDemo(TestCase):
    def test_demo(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        for i in range(10000):
            clock.increment()
            print(clock.str())