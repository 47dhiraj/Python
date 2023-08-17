class Dog:
    total_dogs = []
    def __init__(self, nickname, name):            
        self.nickname = nickname
        self.name = name
        self.total_dogs.append(self.name)

    @classmethod
    def num_dogs(cls):                       
        return (cls.total_dogs)          



pup = Dog(['kutte 1, kamine 1, wafadar 1'], "puppy")               
tim = Dog(['kutte 2, kamine 2, wafadar 2'], "timmy")              


print('Name : ', pup.name, ' Nickname : ', pup.nickname)
print('Name : ', tim.name, ' Nickname : ', tim.nickname)


print(Dog.num_dogs())                            
