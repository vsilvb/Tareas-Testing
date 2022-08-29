from . rewriter import *


class PlusPlusTransformer(NodeTransformer):
    def visit_Call(self, node):
        if node.func.id == 'eval':
            return Call(func=Name(id='literal_eval', ctx=Load()), 
                        args=node.args, 
                        keywords=node.keywords)
        else:
            return node


class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree