import unittest
from model import *
from parser import *
from metrics import *


class TestParser(unittest.TestCase):
    # testing the parser
    def test_number(self):
        ast1 = NumberNode(2)
        ast2 = parser("2")
        self.assertEqual(ast1, ast2)

    def test_sum(self):
        ast1 = AdditionNode(NumberNode(2), NumberNode(3))
        ast2 = parser("(+ 2 3)")
        self.assertEqual(ast1, ast2)

    def test_subs(self):
        ast1 = SubstractNode(NumberNode(3), NumberNode(2))
        ast2 = parser("(- 3 2)")
        self.assertEqual(ast1, ast2)

    def test_mix(self):
        ast1 = SubstractNode(AdditionNode(NumberNode(2), NumberNode(1)), SubstractNode(NumberNode(3), NumberNode(2)))
        ast2 = parser("(- (+ 2 1) (- 3 2))")
        self.assertEqual(ast1, ast2)

    # testing eval
    def test_sum_eval(self):
        ast = parser("(+ 2 3)")
        result = ast.eval()
        self.assertEqual(result, 5)

    def test_subs_eval(self):    
        ast = parser("(- 3 2)")
        result = ast.eval()
        self.assertEqual(result, 1)

    def test_mix_eval(self):
        ast = parser("(- (+ 2 1) (- 3 2))")
        result = ast.eval()
        self.assertEqual(result, 2)

    # testing to string
    def test_to_string(self):
        ast1 = SubstractNode(AdditionNode(NumberNode(2), NumberNode(1)), SubstractNode(NumberNode(3), NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(- (+ 2 1) (- 3 2))")

    # testing visitor
    def test_number_counter(self):
        visitor = NumberCounter()
        ast = parser("(+ (+ 1 1) 2)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)

    def test_addition_counter(self):
        visitor = AdditionCounter()
        ast = parser("(+ (+ 1 1) 2)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 2)


if __name__ == '__main__':
    unittest.main()
