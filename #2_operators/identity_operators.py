#identity operators :

# Example 2 ==> integer data type ma use garda kunnai variable ko same value xa vani tyo duitai variable le same memory lai refer gardo raixa vanni buj vai
a = 100
print(id(a))

b = 100
print(id(b))

result = a is b   #memory location compare gareko
print(result)



# Example 2  ==> but list ko case  ma chai same memory refer gardaina

a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))

result = a is b   #memory location compare gareko
print(result)
