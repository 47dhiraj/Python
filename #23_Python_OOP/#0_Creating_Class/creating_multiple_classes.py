# Example of working with multiple related class ...

class Student:                                     # Student class
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:                                       # Course class
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []                          

    def add_student(self, student):                
        if len(self.students) < self.max_students:
            self.students.append(student)           


    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()           

        return value/len(self.students)


s1 = Student("John", 24, 80)
s2 = Student("Doe", 24, 70)
s3 = Student("David", 24, 60)
s4 = Student("Michael", 24, 75)
s5 = Student("Jimmy", 24, 85)
s6 = Student("Timmy", 24, 90)




course1 = Course('Science', 2)                    
course1.add_student(s1)
print(course1.students[0].name)             
course1.add_student(s2)
print(course1.students[1].name)
print(course1.get_average_grade())

course1.add_student(s3)                             
print(course1.get_average_grade())                 





course2 = Course('Math', 3)                          
course2.add_student(s3)
print(course2.students[0].name)                     
course2.add_student(s4)
print(course2.students[1].name)
course2.add_student(s5)
print(course2.students[2].name)
print(course2.get_average_grade())

course2.add_student(s6)                       
print(course2.get_average_grade())                 





