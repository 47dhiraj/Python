text = "this is not the end this is not the begining dhiraj"

# String Functions
print(len(text))                            # string ko length provide garcha
print(text.endswith("ing"))
print(text.count("t"))                      # t kati choti aayo count garcha
print(text.capitalize())                    # first chararcter lai capital mai laijancha
print(text.casefold())                      # string lai lower case ma laijancha
print(text.lower())                         # string lai lower case ma laijancha
print(text.upper())                         # string lai upper case ma laijancha
print(text.find("end"))                     # index positioning dincha
print(text.replace("dhiraj", "kafle"))      # string ma vayeko word lai arko word le replace gareko



# using len method of string
name="Dhiraj"
a=len(name)
print("Length of the String is:",a)
print (a)


#One way For getting first character of the string
c=name[0]
print("First character of the string is:",c)

#Next way For getting first character of the string
c=name[len(name)-len(name)]
print("Last character of the string is:",c)


#For getting last character of the string
c=name[len(name)-1]
print("Last character of the string is:",c)

#For getting last character of the string
c=name[-1]
print("Last character of the string is:",c)