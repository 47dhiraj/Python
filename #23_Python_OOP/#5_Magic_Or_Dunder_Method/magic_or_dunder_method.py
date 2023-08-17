class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):                                         
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):                             
        self.pay = int(self.pay * self.raise_amt)


    def __repr__(self):                                     
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):                                         
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):                                 
        return self.pay + other.pay

    def __len__(self):                                     
        return len(self.fullname())


emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jimmy', 'Jimmer', 60000)


# for use of __repr__() magic method
print(repr(emp_1))
print(emp_1.__repr__())
print(repr(emp_2), '\n')
print(emp_2.__repr__())


# for use of __str__() magic method
print(emp_1)
print(str(emp_1))
print(emp_1.__str__())
print(str(emp_2))
print(emp_2.__str__())


# for use of __add__() magic method
print(emp_1 + emp_2)

# for use of __len__() magic method
print(len(emp_1))
