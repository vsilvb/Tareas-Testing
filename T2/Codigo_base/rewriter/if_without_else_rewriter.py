from curses.ascii import NUL
from . rewriter import *

class IfWithoutElseTransformer(NodeTransformer):
    def visit_If(self, node: IfExp):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if isinstance(node.orelse[0], Pass):
            statements.orelse = []
        return statements


class IfWithoutElseeRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfWithoutElseTransformer().visit(ast))
        return new_tree
