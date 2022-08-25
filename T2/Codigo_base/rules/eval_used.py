from . rule import *


class EvalVisitor(WarningNodeVisitor):
    def visit_Call(self, node):
        if node.func.id == 'eval':
            self.addWarning('EvalWarning', node.lineno, 'eval should not be used!!')
        NodeVisitor.generic_visit(self, node)


class EvalUsedRule(Rule):
    def analyze(self, ast):
        visitor = EvalVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
