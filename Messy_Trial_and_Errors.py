#A lis is a collection of element in a given order
L=[1,3,4]
L1=['Cash','Purpose']
L2=[1,'Cash',True]
Stuff=[[1,2,6],'Foo',3,False]    
#Access using index and bracket notation 
print (Stuff)       #the whole bracket will be printed
print (Stuff[0])    #for an element
name = 'Banana'
print(name)         # prints Banana
print(name[0])      # prints B
len(name)           # length of string

for letters in name: 
    print (letters)
#whatever we can do with list we can do with string
#the elements of A list is chagneable - mutate but for string not!   
List=[1,3,4]
L[0]=5
print(List)
name[0] = 'm'       #strings are immutable(but there are some functions for do so)
n =5
MA= range(5)
MA=[0,1,2,3,4]
#use the for loop with an index
stuff=[[1,2,6],'Foo',3,False]
n=len(stuff)
for i in range(n):
    print(Stuff[i])
#Same but not really efficient
i = 0
for thing in Stuff:
    print(thing)
    i=i+1
####################################################################################
#List Creation
from calendar import SATURDAY

stuff=list()    #constructor 
print(stuff)    #outputs empty []
#Stuff [0]= 'Book'      #outputs error because it has no size
stuff.append('Book')
print(stuff)

Stuff.append(99)
print (Stuff)

some = [1,3,8,7,-20]
len(some)
max(some)
min(some)
some.sort()

# LIST SLICING
print (some[3])     # prints some at index 3 : which is 7
print (some[0:3])   # prints index 0 to 2
print (some[0:4])   # prints index 0 to 3
print(some [1:4])   # prints index 1 to 3
print (some [3:])   # prints index 3 to end of list

sub = some[:2]      #form indedx 0 to 1 -> make a sublist named sub 
print(sub)          #[-20,1]
#We can do also concatination
print(some)
third=some+sub
print(third)    

############################### and finally Print hello world

print ("Hello World")

