#list declare
numbers = [1, 2, 3, 4, 5]
#list a reverse indexing possible
numbers[0] # এটার ভ্যালু ১
numbers[-1] # এটার ভ্যালু ৫

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6])#list[start:end:step]
#output: [3, 4, 5, 6]

#we can declare step als
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:8:2])
#output: [1, 3, 5, 7]


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[:5])
#output: [1, 2, 3, 4, 5]


#list Method
#append -insert a value at the end of list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
# output: [1, 2, 3, 4, 5, 6]

#insert -we can insert any value at any position 
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 100)
print(numbers)
# output: [1, 2, 100, 3, 4, 5]

#remove-we can remove a element from a list
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)
# output: [1, 2, 4, 5]

#index-value dile oitar index return korbe
#https://docs.python.org/3/tutorial/datastructures.html