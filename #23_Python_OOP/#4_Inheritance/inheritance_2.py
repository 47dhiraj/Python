class Dog():
    def __init__(self, name, age):          
        self.name = name
        self.age = age

    def speak(self):
        print('Hi i am ', self.name, ' and i am ', self.age, ' years old.')

    def talk(self):
        print('bark')


class Cat(Dog):             
    def __init__(self, name, age, color):   # constructor of cat class
        super().__init__(name, age)        
        # self.name = name              
        # self.age = age                  
        self.color = color           


    # Method Overriding case
    def talk(self):       
        print('meow')



birali = Cat('birali', 2, 'grey')
puppy = Dog('puppy', 3)

birali.speak()
birali.talk()

puppy.speak()
puppy.talk()
