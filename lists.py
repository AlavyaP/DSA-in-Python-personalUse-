# Python List ------->>>>>>  A list is a data structure that holds an ordered collection of items.
'''
alist = [1,'qwerty',45.54,[52,54]]
print(alist)
'''

# Accessing/Traversing in a list
shoppingList = ['Milk','Cheese','Butter']
'''
print(shoppingList[1])
print('Cream' in shoppingList)  # we can use in operator to check if it is available or not ---> it returns True/False
'''

# Traversing in a list
'''
for i in shoppingList:
    print(i) 
'''
 
# Searching in a list 
my_list = [1,2,3,5,4,6,7,8,9,0]
# using IN Operator
'''
if 2 in my_list:
    print(my_list.index(2))
else:
    print(my_list)
'''
# Linear Search
'''
def linearSearch(list,value):
    for i in list:
        if (i == value):
            return (list.index(value))
    return ("The value not Found")

print(linearSearch(my_list,7))
'''

# list Operators/Functions
# ---> "+" concatenation operator
'''
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
'''

# ----> "*" operators for multiplication of elements in a list
'''
a = [1]
a = a*4
print(a)
'''

# len() function  --->>  len() returns count of elements in the List
z = [1,2,3,4,5,6,7,8,9,0]
'''
print(len(z))
'''
# max() function ---->> max() : returns the item with the highest value in the List
'''
print(max(z))
'''
# min() function -->> min() : returns the item with the lowest value in the List
'''
print(min(z))
'''
# sum() function --->> sum() : returns the sum of all items in the List
'''
print(sum(z))
'''

# EXERCISE TO FIND THE AVERAGE 

myList = list()
while (True):
    itm = input("Enter a Number:").lower()
    if itm == 'done':
        break
    else:
        value = float(itm)
        myList.append(value)
        total = sum(myList)
        count = len(myList)
mid = total/count 
print(mid)
    
      