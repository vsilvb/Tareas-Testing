from .rule import *


class DummyIfVisitor(WarningNodeVisitor):
    def visit_If(self, node: If):
        if isinstance(node.test, Constant):
            if node.test.value == True:
                self.addWarning('DummyIfWarning', node.lineno, 'this if does not have any sense!')


class DummyIfRule(Rule):
    def analyze(self, ast):
        visitor = DummyIfVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
