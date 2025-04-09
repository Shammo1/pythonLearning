#if i wanna send a value with a keyword i have to use kwarg

def solve(name,**new):
    
    for i,j in new.items():
        print(i,j) 


solve('saam',apple=3, aam=5)
 
"""" 
 def func( a, b, c):
return a, b, c # return as tuple (a, b, c)
return [a, b, c] # return as list [a, b, c]
return {'a': a, 'b': b} # return as dictionary
"""