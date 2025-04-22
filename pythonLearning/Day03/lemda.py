#syntax
#lambda arguments: expression
add=lambda x,y:x+y
print(add(2,3))
new=[1,23,4,56,7,6]
##map
#squares = list(map(lambda x: x**2,new))
##print(f"{squares}") 

##filter
squares = list(filter(lambda y:y%2==0,new))
print(f"{squares}") 
##sorted