from . rule import *

class FunctionCounterVisitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.attr = []
        self.funcs = 0
        self.funcs_accs = 0

    def visit_FunctionDef(self, node: FunctionDef):
        self.funcs += 1
        if node.name == '__init__':
            for i in node.body:
                if isinstance(i, Assign):
                    if isinstance(i.targets[0], Attribute):
                        self.attr.append(i.targets[0].attr)
        elif 'set' in node.name or 'get' in node.name:
            if len(node.body) == 1:
                if isinstance(node.body[0], Assign):
                    if isinstance(node.body[0].targets[0], Attribute):
                        if node.body[0].targets[0].attr in self.attr:
                            self.funcs_accs += 1
                elif isinstance(node.body[0], Return):
                    if isinstance(node.body[0].value, Attribute):
                        if node.body[0].value.attr in self.attr:
                            self.funcs_accs += 1
                

        
    def conclusion(self):
        return (self.funcs - self.funcs_accs) == 1 and len(self.attr) != 0


class DataClassVisitor(WarningNodeVisitor):
    def __init__(self):
        super().__init__()

    def visit_ClassDef(self, node: ClassDef):
        visitor = FunctionCounterVisitor()
        visitor.visit(node)
        if visitor.conclusion():
            self.addWarning('DataClassWarning', node.lineno, ' class '+ node.name + ' only stores information')
        NodeVisitor.generic_visit(self, node)


class DataClassRule(Rule):
    def analyze(self, ast):
        visitor = DataClassVisitor()
        visitor.visit(ast)
        return visitor.warningsList()