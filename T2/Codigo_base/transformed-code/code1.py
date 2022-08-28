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
        e = 8
        f = d + e
        return 2 + 6 + self.b + c + a

    def doit(self):
        literal_eval('2+2')

    def somethig(self):
        print('something')