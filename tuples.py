# tuples -->> It is a immutable sequence  of Python objects, A Tuple are also comparable and hashable.
# syntax 
newTuple = ('a','b','c','d')
'''
# or
newTuple2 = ('a',)
# or we can just use tuple() operator to create a new tuple

print(newTuple)
print(newTuple2)
'''

# Access element in a tuple 
'''
print(newTuple[1])
# slice operator
print(newTuple[::2])
'''

# Traversing a Tuple
'''
for i in range (len(newTuple)):
    # print(i)
    print(newTuple[i])
'''

# Searching in a Tuple
'''
print('a' in newTuple)  #-->> output == True
print('f' in newTuple) #-->> output == False

# index method
print(newTuple.index('a'))

# method 3 
def searchTuple(tuple,value):
    for i in range (0,len(tuple)):
        if tuple[i] == value:
            return(f'The {value} was found at {i} index')
    return("Value not Found")

print(searchTuple(newTuple,'c'))
'''

# Tuple Operators/Functions
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

# concatenation
'''
print(myTuple + myTuple1) 
'''

# star operator (*) -->> each element of a tuple will be repated each time (for example 4 times)
'''
print(myTuple * 4)
'''

# Count Method -->> count the number of times a element is present in a tuple 
'''
print(myTuple.count(2)) 
'''

# len function -->> return the length of the tuple 
'''
print(len(myTuple))
'''

# max/min function -->> returns the maximum/minimum element of the tuple 
'''
print(max(myTuple))
print(min(myTuple))
'''
# tuple is also build in fuction in python library
