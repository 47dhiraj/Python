class Employee:
    num_of_emps = 0
    raise_amt = 1.5

    def __init__(self, first, last, pay, raise_amout= None):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1                         
        if raise_amout != None:
            self.raise_amt = raise_amout


    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)              
        # self.pay = int(self.pay * Employee.raise_amt)          
        return self.pay


# For checking the no. of objects created
print('Number of Employees :', Employee.num_of_emps)

# emp_1 = Employee('John', 'Doe', 50000)
# emp_2 = Employee('Agent', '47', 50000)

# # print(Employee.__dict__)                                   

# print(emp_1.__dict__)                                     
# print(emp_2.__dict__)                                    
#
# print(emp_1.apply_raise())
# print(emp_2.apply_raise())




# yedi kunai employee lai raise amout garni kunai lai nagarni ho vani yesari employee object banaudai kunai lai raise amout halera banaune, kunai lai na hali banaune
emp_1 = Employee('John', 'Doe', 50000, 2)           # yedi, employee object create garda nai specific raise amount halera create gareko cha vani, so yesle class variable ma vako initial  1.5  raise_amount vanni value lai override garera 2 garaucha
emp_2 = Employee('Agent', '47', 50000)              # yedi, employee object create garda nai specific raise amount halera create gareko chaina vani, so yesle class variable ma vako initial  1.5  raise_amount nai ligi rakhya huncha

# print(Employee.__dict__)

print(emp_1.__dict__)
print(emp_1.raise_amt)
print(emp_1.apply_raise())

print(emp_2.__dict__)
print(emp_2.raise_amt)
print(emp_2.apply_raise())




# At Final, checking the no. of employees created
print('Number of Employees :', Employee.num_of_emps)