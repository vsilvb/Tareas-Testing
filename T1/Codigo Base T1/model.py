# model cualquier nodo del arbol
class Node:
    # formatea la expresion en un string
    def to_string(self):
        pass

    # evalua la expresion
    def eval(self):
        pass

    # acepta la visita de un visitor
    def accept(self, visitor):
        pass

    # verifica si un nodo es igual a otro
    def __eq__(self, other):
        return self.__class__ == other.__class__


# nodos literales normalmente son los valores primitivos
# string, entero o boolean
class LiteralNode(Node):
    def __init__(self, val):
        self.value = val

    def to_string(self):
        pass

    def eval(self):
        return self.value

    def accept(self, visitor):
        visitor.visit_Literal(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value


# un numero dentro del programa
class NumberNode(LiteralNode):
    def accept(self, visitor):
        visitor.visit_Number(self)

    def to_string(self):
        return "" + str(self.value)


# operadores
class OperatorNode(Node):
    def __init__(self, sym):
        self.symbol = sym

    def accept(self, visitor):
        visitor.visit_Operator(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.symbol == other.symbol


# operador binario
class BinaryOperatorNode(OperatorNode):
    def __init__(self, leftNode, rightNode, sym):
        super().__init__(sym)
        self.leftNode = leftNode
        self.rightNode = rightNode

    def to_string(self):
        return "(" + self.symbol + " " + self.leftNode.to_string() + " " + self.rightNode.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_BinaryOperator(self)

    def __eq__(self, other):
        if self.__class__ != other.__class__: return False
        if self.symbol != other.symbol: return False
        if self.leftNode != other.leftNode: return False
        if self.rightNode != other.rightNode: return False
        return True


# operador suma binaria
class AdditionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(AdditionNode, self).__init__(leftNode, rightNode, "+")

    def eval(self):
        return self.leftNode.eval() + self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Addition(self)


# operador resta binaria
class SubstractNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(SubstractNode, self).__init__(leftNode, rightNode, "-")

    def eval(self):
        return self.leftNode.eval() - self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Substract(self)

# operador unitario
class UnaryOperatorNode(OperatorNode):
    def __init__(self, Node, sym):
        super().__init__(sym)
        self.Node = Node

    def to_string(self):
        return "(" + self.symbol + " " + self.Node.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_UnaryOperator(self)

    def __eq__(self, other):
        if self.__class__ != other.__class__: return False
        if self.symbol != other.symbol: return False
        if self.Node != other.Node: return False
        return True


# operador suma unitaria
class PlusPlusNode(UnaryOperatorNode):
    def __init__(self, Node):
        super(PlusPlusNode, self).__init__(Node, "++")

    def eval(self):
        return self.Node.eval() + 1

    def accept(self, visitor):
        visitor.visit_PlusPlus(self)


# operador resta unitaria
class MinusMinusNode(UnaryOperatorNode):
    def __init__(self, Node):
        super(MinusMinusNode, self).__init__(Node, "--")

    def eval(self):
        return self.Node.eval() - 1

    def accept(self, visitor):
        visitor.visit_MinusMinus(self)


# visitor
class Visitor:
    # los nodos computestos deben propagar la visita a los subnodos
    def visit_Addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Substract(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Number(self, node):
        pass

    def visit_PlusPlus(self, node):
        node.Node.accept(self)

    def visit_MinusMinus(self, node):
        node.Node.accept(self)
