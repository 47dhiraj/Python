# user aafaile exceptions banaune
class CustomError(Exception):               # yo line ma '(Exception)' chai python le diyeko class inheret gareko
    def __init__(self, message, errors):    # CustomError vanni hamile banayeko class ko constructor ho

        super().__init__(message)           # call the base class constructor with message as parameter

        #now for your custom code......
        self.errors = errors




a = 12
if a > 10:
    raise CustomError("Not good", "must be less than 10")