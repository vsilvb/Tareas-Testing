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
        a -= b
        e = 8
        f = d + e
        a += b
        return 2 + 6 + self.b + c + a

    def doit(self):
        literal_eval('2+2')
        if self.b > 5:
            print('mayor a 5')
            if self.a == '4':
                print('probando')
        elif self.b == 5:
            pass

    def somethig(self):
        print('something')