class Person1:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getName(self):
        return self.firstName

    def setName(self, newName):
        self.firstName = newName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newName):
        self.lastName = newName

class Person2:

    def getName(self):
        return self.firstName

    def setName(self, newName):
        self.firstName = newName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newName):
        self.lastName = newName

class Person3:

    def __init__(self, firstName, lastName, a):
        self.firstName = firstName
        self.lastName = lastName
        self.a = a

    def getName(self):
        return self.firstName

    def setName(self, newName):
        self.firstName = newName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newName):
        self.lastName = newName

    def metodo(self, a, b):
        c = a + b
        return c