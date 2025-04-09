""""#you can set default peremiter in python function
def sum(a,b,c=0):
  return a+b+c

x=int(input())
y=int(input())
ans=sum(x,y)#here i have only send 2 peremiter values if i dont send any value for c it will take c=0 as value
print(ans)"""

# if i dont know how much values i have to send in my function then i can use *args ,
# now i can send how many values i wanna send
def code(*args):
    sum=0
    for i in args:
        sum+=i   
    return sum 

x=int(input())
y=int(input())
z=code(x,y)
print(z)