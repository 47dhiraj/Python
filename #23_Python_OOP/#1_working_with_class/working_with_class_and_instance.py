class Employee:

    def __init__(self, first, last, pay):           
        self.first = first                        
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):                            
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('John', 'Doe', 50000)           

emp_2 = Employee('Agent', '47', 60000)          



# print(id(emp_1.first))                 
print(emp_1.first)
print(emp_1.fullname())
# Alternative way of calling method inside class
# print(Employee.fullname(emp_1))

# print(id(emp_2.first))                         
print(emp_2.first)
print(emp_2.fullname())
# Alternative way of calling method inside class
# print(Employee.fullname(emp_2))
