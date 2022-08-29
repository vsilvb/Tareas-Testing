
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.b = 5
        self.a = 'hey'

    def fullName(self):
        a = 2
        b = 3
        c = 6
        d = 7
        a += b
        a = a - b
        e = 8
        f = d + e
        a = a + b
        return 2 + 6 + self.b + c + a

    def doit(self):
        eval("2+2")

    def somethig(self):
        if True:
            print("something")

