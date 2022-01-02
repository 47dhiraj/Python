# Python map() method accepts a function as a parameter and returns a list.

# Example 1 :

lst = [10, 50, 75, 83, 98, 84, 32]

res = list(map(lambda x: x, lst))

print(res)

'''
In the above snippet of code, lambda x:x function is provided as input to the map() function. 
The lambda x:x will accept every element of the iterable and return it.


The input_list (lst) is provided as the second argument to the map() function. 
So, the map() function will pass every element of lst to the lambda x:x function and return the elements.
'''