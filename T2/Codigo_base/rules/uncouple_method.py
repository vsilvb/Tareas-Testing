from . rule import *


class AttributeNodeCounterVisitor(NodeVisitor):
    def __init__(self):
        self.attrs = 0

    def visit_Attribute(self, node: Attribute):
        self.attrs = self.attrs + 1
        
    def total(self):
        return self.attrs


class UnCoupledMethodVisitor(WarningNodeVisitor):
    
    def visit_FunctionDef(self, node: FunctionDef):
        visitor = AttributeNodeCounterVisitor()
        visitor.visit(node)
        if visitor.total() == 0:
            self.addWarning('UnCoupledMethodWarning', node.lineno, 'method ' + node.name + ' does not use any attribute')
        NodeVisitor.generic_visit(self, node)


class UnCoupledMethodRule(Rule):
    def analyze(self, ast):
        visitor = UnCoupledMethodVisitor()
        visitor.visit(ast)
        return visitor.warningsList()