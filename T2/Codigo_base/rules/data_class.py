from . rule import *

class FunctionCounterVisitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.funcs = 0

    def visit_FunctionDef(self, node: FunctionDef):
        self.funcs = self.funcs + 1
        
    def total(self):
        return self.funcs


class DataClassVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()

    def visit_ClassDef(self, node: ClassDef):
        visitor = FunctionCounterVisitor()
        visitor.visit(node)
        if visitor.total() == 0:
            self.addWarning('DataClassWarning', node.lineno, 'data class '+ node.name + ' has no methods')
        NodeVisitor.generic_visit(self, node)


class DataClassRule(Rule):
    def analyze(self, ast):
        visitor = DataClassVisitor()
        visitor.visit(ast)
        return visitor.warningsList()