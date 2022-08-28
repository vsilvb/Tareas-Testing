from .rule import *


class AttributeNameVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        
    def visit_Assign(self, node: Assign):
        
        if isinstance(node.targets[0], Attribute):
            if len(node.targets[0].attr) == 1:
                self.addWarning('SusupiciousVariableNameWarning', node.lineno, 'variable '+ node.targets[0].attr + ' has an supicious name ')
        elif isinstance(node.targets[0], Name):
            if len(node.targets[0].id) == 1:
                self.addWarning('SusupiciousVariableNameWarning', node.lineno, 'variable '+ node.targets[0].id + ' has an supicious name ')
        NodeVisitor.generic_visit(self, node)


class SuspiciousVariableNameeRule(Rule):
    def analyze(self, ast):
        visitor = AttributeNameVisitor()
        visitor.visit(ast)
        return visitor.warningsList()