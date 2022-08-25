from ast import *
from pprint import pprint


class RewriterCommand:
    def apply(self, ast):
        # as default return the same ast without any modification
        return ast
