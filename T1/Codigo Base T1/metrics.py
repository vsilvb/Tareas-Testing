from model import *
# visitador que cuenta cuantos nodo de tipo number existen en el arbol


class NumberCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_Number(self, node):
        self.counter = self.counter + 1

    def total(self):
        return self.counter


# visitador que cuenta cuantos nodo de tipo addition existen en el arbol
class AdditionCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_Addition(self, node):
        # los nodos compuestos deben propagar la visita
        node.leftNode.accept(self)
        node.rightNode.accept(self)
        self.counter = self.counter + 1

    def total(self):
        return self.counter

# visitador que cuenta cuantos nodos de tipo operador unitario existen en el arbol
class UnaryOperatorCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_PlusPlus(self, node):
        # los nodos compuestos deben propagar la visita
        node.Node.accept(self)
        self.counter = self.counter + 1

    def visit_MinusMinus(self, node):
        # los nodos compuestos deben propagar la visita
        node.Node.accept(self)
        self.counter = self.counter + 1

    def total(self):
        return self.counter
