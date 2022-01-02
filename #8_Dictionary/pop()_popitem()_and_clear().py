# For pop() method
'''
The pop() method removes the specified item from the dictionary.
The return value of the pop() method is the value of the removed item.
'''

# Example 1:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car)

x = car.pop("model")
print(x)

print(car)


# For popitem() method
'''
The popitem() method removes the item that was last inserted into the dictionary.
The return value of the popitem() method is the value of the removed item.
'''

laptop = {
  "brand": "hp",
  "model": "pavillion notebook",
  "year": 2015
}
print(laptop)

x = laptop.popitem()
print(x)

print(laptop)


# For clear() method
'''
The clear() method removes all the elements from a dictionary.
'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

car.clear()
print(car)




