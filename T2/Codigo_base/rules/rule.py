from ast import *
from pprint import pprint

class Warning:
    def __init__(self, name, line, description):
        self.name = name
        self.lineNumber = line
        self.description = description
    def wprint(self):
        print("["+ str(self.lineNumber) +"] " + self.name + " - " + self.description)
        
class Rule:
    def __init__(self):
        self.warningsList = []
    # debe retornar una lista de objetos warnings
    def analyze(self,ast):
        pass
    def warnings(self):
        return self.warningsList

class WarningNodeVisitor(NodeVisitor):
    def __init__(self):
        self.warnings = []
    
    def addWarning(self, name, lineo, description):
        self.warnings.append(Warning(name,lineo,description))

    def warningsList(self):
        return self.warnings