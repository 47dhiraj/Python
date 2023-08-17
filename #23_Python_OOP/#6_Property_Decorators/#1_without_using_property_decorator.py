class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Johnny', 'Doeyy')
print(emp_1.first)
print(emp_1.last)

emp_1.first = 'John'
emp_1.last = 'Doe'

print(emp_1.email())
print(emp_1.fullname())

