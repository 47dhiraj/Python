class Pet:                                   
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} & i am {self.age} years old.")

    def speak(self):
        print("I don't speak.")




class Dog(Pet):                                 
    def __init__(self, name, age, color):
        super().__init__(name, age)            
        # Alternative code for constructor inheritance
        # self.name = name
        # self.age = age
        self.color = color

    def show(self):
        print(f"I am {self.name} & i am {self.age} years old & i looks {self.color}.")

    def speak(self):
        print("Bark")

class Cat(Pet):                                 
    def speak(self):
        print("Meow")

class Fish(Pet):                               
    pass


p = Pet("Tim", 20)
p.show()
p.speak()

d = Dog("puppy", 5, "grey")
d.show()
d.speak()

c = Cat("birli", 5)
c.show()
c.speak()

f = Fish("macha", 5)
f.show()
f.speak()






