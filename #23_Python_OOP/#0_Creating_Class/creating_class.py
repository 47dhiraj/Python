class Dog():                                     

    def __init__(self, naam, umer):               
        # print(naam)                         
        # print(umer)                         
        self.name = naam                         
        self.age = umer                           
        # print(self.name)
        # print(self.age)


    # bark() chai dog class ko method ho
    def bark(self):                       
        print(self.name, 'is barking & his age is ', self.age)

    # change_age() chai dog class ko method ho
    def change_age(self, umer):
        self.age = umer





puppy = Dog('Puppy', 2)                          
tommy = Dog('Tommy', 3)                             

print(puppy.age)                                 
print(tommy.age)
# Cant do this ==> print(age)                                      

puppy.change_age(4)
tommy.change_age(6)

puppy.bark()
tommy.bark()

