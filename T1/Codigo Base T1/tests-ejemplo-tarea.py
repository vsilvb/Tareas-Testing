import unittest
from model import *
from parser import parser, splitArgs
from metrics import *


class TestParser(unittest.TestCase):
    # test para la tarea
    # debe agregar las clases y modificar los metodos necesarios
    # para que los siguientes test compilen y pasen
    # usted puede agregar mas tests
    def test_pp(self):
        ast1 = PlusPlusNode(NumberNode(2))
        ast2 = parser("(++ 2)")
        self.assertEqual(ast1, ast2)

    def test_pp_eval(self):
        ast = parser("(++ 2)")
        result = ast.eval()
        self.assertEqual(result, 3)

    def test_mm_eval(self):
        ast = parser("(-- 3)")
        result = ast.eval()
        self.assertEqual(result, 2)

    def test_mix(self):
        ast = parser("(+ (++ 1) (++ 1))")
        result = ast.eval()
        self.assertEqual(result, 4)
    
    def test_to_string2(self):
        ast1 = PlusPlusNode(MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(++ (-- 2))")

    def test_to_string3(self):
        ast1 = AdditionNode(PlusPlusNode(NumberNode(1)),MinusMinusNode(NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(+ (++ 1) (-- 2))")
    
    def test_unary_counter(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(+ (+ (++ 1) (++ 1)) (- 2 (-- 3)))")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)

    def test_unary_counter2(self):
        visitor = UnaryOperatorCounter()
        ast = parser("(++ 1)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 1)


if __name__ == '__main__':
    unittest.main()
