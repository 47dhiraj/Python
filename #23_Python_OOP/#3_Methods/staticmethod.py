class Dog:
    dogs = []                              

    def __init__(self, name):               
        self.name = name
        self.dogs.append(self)


    @staticmethod                          
    def bark(n):                        
        for _ in range(n):
            print('Bark !')


Dog.bark(5)                
