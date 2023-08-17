class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property                                   # @property decorator cha vani tyo Getter ho (i.e getter ko help batw property ko value get garna sakincha )
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property                                   # @property decorator cha vani tyo Getter ho
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter                            # @property_name.setter cha vani tyo setter ho (i.e setter ko help batw property ko value set garna sakincha )
    def fullname(self, name):
        first, last = name.split(' ')           # split name on whitespace
        self.first = first
        self.last = last

    @fullname.deleter                           # @property_name.deleter cha vani tyo deleter ho (i.e deleter ko help batw property ko value delete garna sakincha)
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('Johnny', 'Doey')

emp_1.fullname = "John Doe"                         # fullname set gareko using @fullname.setter

print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname                                  # fullname delete gareko using @fullname.deleter
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)