
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
        if a > 0:
            a = b + 3
        else:
            pass
        return 2 + 6 + self.b + c + a

    def doit(self):

        if self.b > 5:
            print('B es mayor a 5')

            if self.a == '4':
                print('A es 4')

            else:
                pass

        elif self.b == 5:
            pass

        else:
            
            pass

    def somethig(self):
        if True:
            print("something")
        else: 
            pass

