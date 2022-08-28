from .rule import *

class AssignVariableVisitor(NodeVisitor):
    def __init__(self):
        self.assign = []
        self.used = []
        self.unused =[]

    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], Name):
            if node.targets[0].id not in self.assign:
                self.assign.append(node.targets[0].id)

class UsedVariableVisitor(NodeVisitor):
    def __init__(self):
        self.used =[]

    def visit_BinOp(self, node: BinOp):
        if isinstance(node.left, Name):
            if node.left.id not in self.used:
                self.used.append(node.left.id)
        if isinstance(node.right, Name):
            if node.right.id not in self.used:
                self.used.append(node.right.id)
        NodeVisitor.generic_visit(self, node)


class MethodVisitor(WarningNodeVisitor):
    
    def visit_FunctionDef(self, node: FunctionDef):
        visitor_used = UsedVariableVisitor()
        visitor_used.visit(node)
        visitor_assign = AssignVariableVisitor()
        visitor_assign.visit(node)
        for i in visitor_assign.assign:
            if i not in visitor_used.used:
                self.addWarning('NeverReadedVariableWarning', node.lineno, 'variable ' + i + ' isn\'t used in method ' + node.name )
        NodeVisitor.generic_visit(self, node)


class NeverReadedRule(Rule):
    def analyze(self, ast):
        visitor = MethodVisitor()
        visitor.visit(ast)
        return visitor.warningsList()