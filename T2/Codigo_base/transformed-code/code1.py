class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def fullName(self):
        return self.firstName + self.lastName

    def doit(self):
        literal_eval('2+2')

    def somethig(self):
        print('something')