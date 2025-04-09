#basic syntex
#range([start], stop,[step])

#for i in range(10,20,2) :
   # print(i)
   
 #PRINT ALL THE EVEN NUMBER FROM 1-20;
for i in range(1,20,1):
    if i%2==0 :
        print(i)
    
#print all the numbers which are divisibale by 3,7 from 1 to 300
    for i in range(1, 300):
        if i % 3 == 0 and i % 7 == 0:
            print(i)
# Example: Print numbers from 1 to 5, skipping even numbers using a for loop with continue statement
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)
#break statement
for i in range(1,10):
    if i>5:
        break
    print(i)
    
#for loop in char
word="python"
for i in word :
    print(i)

#for in list
list=[1,3,2,12,323,3]
for i in list:
    if i==323 :
        continue
    print(i)