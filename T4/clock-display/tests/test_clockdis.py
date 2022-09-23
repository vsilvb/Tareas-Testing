from src.clock_factory import *
from unittest import TestCase

class TestClockDisplay(TestCase):
    def setUp(self):
        self.clock = ClockDisplay([24,60])
        self.assertEqual(self.clock.__init__.__annotations__['return'], None)
        

    def test_increment(self):
        currentDisplay = len(self.clock.numbers) - 1
        
        j = -1
        for i in range(1390):
            if i % 60 == 0:
                j += 1

            if j % 24 == 0:
                j = 0

            self.assertEqual(self.clock.numbers[currentDisplay].value, i % 60)
            self.assertEqual(self.clock.numbers[currentDisplay - 1].value, j)
            self.clock.increment()

        

    def test_str(self):
        str = self.clock.str()
        self.assertEqual(str, '00:00')
        self.clock.increment()
        str = self.clock.str()
        self.assertEqual(str, '00:01')
        
        for i in range(59):
            self.clock.increment()
        
        str = self.clock.str()
        self.assertEqual(str, '01:00')
    
    def test_clone(self):
        clone = self.clock.clone()
        for i in range(len(self.clock.numbers)):
            self.assertEqual(clone.numbers[i].value, 0)
        
    def test_invariant(self):
        self.assertEqual(self.clock.invariant(),True)
        for i in range(60):
            self.clock.increment()
            self.assertEqual(self.clock.invariant(),True)
        
        self.clock.numbers[1].value = 60
        self.assertEqual(self.clock.invariant(),False)
        self.clock.numbers[0].value = 25
        self.assertEqual(self.clock.invariant(),False)
