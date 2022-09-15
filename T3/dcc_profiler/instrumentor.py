from ast import *
import threading
from multiprocessing.dummy import Array
import os

class Instrumentor(NodeTransformer):
    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        injected_code = 'Profile.record(\''+ transformedNode.name+'\',['
        i = 0
        for arg in transformedNode.args.args:
            if i == 0:
                injected_code = injected_code + arg.arg
            else:
                injected_code = injected_code + ', '+ arg.arg
            i = i + 1
        injected_code = injected_code + '])'
        
        ast_to_inject = parse(injected_code)
        
        if isinstance(transformedNode.body, list):
            transformedNode.body.insert(0, ast_to_inject.body[0])
        else:
            transformedNode.body = [ast_to_inject.body[0], node.body]
        
        fix_missing_locations(transformedNode)
        
        return transformedNode

class Profile:
    __singleton_lock = threading.Lock()
    __singleton_instance = None
    @classmethod
    def getInstance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance

    @classmethod
    def reset(cls):
        cls.__singleton_instance = None

    @classmethod
    def record(cls, functionName, args):
        cls.getInstance().ins_record(cls, functionName,args)
    
    # instance method
    def __init__(self):
        self.functions_called = {}
        
    def ins_record(self, cls, functionName, args):
        if functionName not in self.functions_called:
            self.functions_called[functionName] = [args]
        else:
            self.functions_called[functionName].append(args)

    def printReport(self):
        print("-- executed methods --")
        for functionName in self.functions_called:
            repetido = True
            arg_ini = self.functions_called[functionName][0]
            for arg in self.functions_called[functionName]:
                if arg_ini != arg:
                    repetido = False
            if repetido:
                print(functionName)
            


    
def instrument(ast):
    visitor = Instrumentor()
    return  fix_missing_locations(visitor.visit(ast))