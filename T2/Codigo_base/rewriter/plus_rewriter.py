from . rewriter import *


class PlusPlusTransformer(NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node.value, BinOp):
            if not isinstance(node.value.left, Constant):
                if node.targets[0].id == node.value.left.id:
                    if isinstance(node.value.op, Add):
                        return AugAssign(target=Name(id=node.targets[0].id, ctx=Store()), op=Add(), value=node.value.right)
                    elif isinstance(node.value.op, Sub):
                        return AugAssign(target=Name(id=node.targets[0].id, ctx=Store()), op=Sub(), value=node.value.right)
            if not isinstance(node.value.right, Constant):
                if node.targets[0].id == node.value.right.id:
                    if isinstance(node.value.op, Add):
                        return AugAssign(target=Name(id=node.targets[0].id, ctx=Store()), op=Add(), value=node.value.left)
                    elif isinstance(node.value.op, Sub):
                        return AugAssign(target=Name(id=node.targets[0].id, ctx=Store()), op=Sub(), value=node.value.left)
        return node


class PlusPlusRewriterCommand(RewriterCommand):
    def apply(self, ast):
        new_tree = fix_missing_locations(PlusPlusTransformer().visit(ast))
        return new_tree