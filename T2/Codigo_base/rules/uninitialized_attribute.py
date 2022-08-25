from . rule import *


class AttributeUsageVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()
        self.initialized = []

    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Attribute):
            self.initialized.append(node.targets[0].attr)
        NodeVisitor.generic_visit(self, node)
    
    def visit_Attribute(self, node: Attribute):
        if self.initialized.count(node.attr) == 0:
            self.addWarning('UninitilizeAttrWarning', node.lineno, 'attribute '+ node.attr + ' was not initialized')
        NodeVisitor.generic_visit(self, node)


class UninitialiedAttributeRule(Rule):
    def analyze(self, ast):
        visitor = AttributeUsageVisitor()
        visitor.visit(ast)
        return visitor.warningsList()