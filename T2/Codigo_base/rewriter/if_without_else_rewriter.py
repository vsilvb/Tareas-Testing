from . rewriter import *


class IfWithoutElseTransformer(NodeTransformer):
    def visit_If(self, node):
        NodeTransformer.generic_visit(self, node)
        statements = node
        if isinstance(node.test, Constant):
            if node.test.value == True:
                # el body puede ser una lista de statement
                statements = node.body
        return statements


class IfWithoutElseRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(IfWithoutElseTransformer().visit(ast))
        return new_tree
