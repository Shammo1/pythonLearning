#set insert uniqe and make it sorted order element
myset={1,2,34,2,3,34,3,3}
#print(myset)
#output:{1, 2, 3, 34}
#we can do (|)union and (&)intersection of two sets
myset2={1,2,3,4}
#outset=myset | myset2
#print(outset)

outset=myset & myset2
print(outset)
#output:{1, 2, 3}