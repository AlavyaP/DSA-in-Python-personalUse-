# for creating an array in python 

from array import *

array1 = array('i',[1,2,3,4,6,5,7,8,9,0])
# arrayname = array('datatype',[Values]) ----->>> Syntax

# print(array1)


# insertion of element in a array

# array1.insert(1,22)
# arrayname.insert(index,element)
# print(array1)


# transversing in a array
''' 
def transversArray(arr):
    for i in (arr):
        print(i)
        
transversArray(array1)

'''


# Access a element in a array
'''
def accessArray(array,index):
    if (index >= len(array)):
        print("index not available")
    else:
        print(array[index])
        
accessArray(array1,10)
'''
# Searching in a array
'''
def searchArray(arr,ele):
    for index in (arr):
        if (index == ele):
            return arr.index(ele)
    return("Elemet is not in this array")  
              
print(searchArray(array1,3))
'''

# Deleting a element from a array
'''
array1.remove(0)
array1.remove(9)
array1.remove(7)
print(array1)
'''

# ----------------------------------------------------------------------------------
# Questions from DSA Udemy                                              ||||||||||||
# ----------------------------------------------------------------------------------

# 1] create an array and transverse

'''
from array import *
'''
arr1 = array('i',[1,2,3,4,5,6,7])

# transverse 
'''
def transverseArray(arr):
    for i in (arr):
        print(i)
transverseArray(arr1)
'''

# 2] Acces individual elemt of the array
# print(arr1[3]) --------------------------------------||||||||||||||||

# 3] Append a value in an array
# arr1.append(8) --------------------|||||||||||||||||||||||
# print(arr1)

# 4] Insert a element in a array
'''
arr1.insert(2,8)
print(arr1)
'''

# 5] Add element using extend
''' 
arr2 = array('i',[8,9,10])
arr1.extend(arr2)
print(arr1)
'''

# 6] Add item from the list into an array using fromlist() method
'''
list_arr = [77,88,99,100]
arr1.fromlist(list_arr)
print(arr1)
'''

# 7] Remove a element from an array
'''
arr1.remove(7)
print(arr1)
'''

# 8] Remove a element using pop method
'''
arr1.pop(5)
print(arr1)
'''
# 9] Fetch any element through its index using index() method 
'''
print(arr1[6]) -------------------------|||||||||||||||||||
print(arr1.index(7))
'''

# 10] Reverse a array ---------------------||||||||||||||||||
'''
arr1.reverse()
print(arr1)
'''

# 11] Get array buffer information through buffer_into() method
# print(arr1.buffer_info()) -----||||||||||||||_--------------

# 12] Check the occurrance of an element using count() method
'''
arr2 = array('i',[1,2,3,4,3,3,3,3,3,3,3,1,3,3])
print(arr2.count(3))
'''

# 13] Convert an array to python list using tostring()
'''
# |||||||||||||||||||||||
# No use as python has removed thr tostring from python 3.9+
# |||||||||||||||||
'''

# 14] Convert an array to python list using tolist()
# print(arr1.tolist()) --------------||||||||||||||

# 15] Append a string to char array using fromstring() method
'''
# |||||||||||||||||||||||
# No use as python has removed thr tostring from python 3.9+
# |||||||||||||||||
'''

# 16]Slice Element from an array
# print(arr1[1:4])
# --------------------------------\\\\\--------------------\\\\\\\\\\\\\\-------------------------------------\\\\\\\\

'''
TWO DIMENSIONAL ARRAY
'''
# --------------------------------\\\\\--------------------\\\\\\\\\\\\\\-------------------------------------\\\\\\\\


import numpy as np

twoDarray = np.array([ [11,12,13,14], [15,16,17,18], [19,20,21,22] ])
print(twoDarray)


'''
# insertion in 2 dimensional array
newArray = np.insert(twoDarray,0, [[52,53,54,55]],axis=0)
print(newArray)

# using append method
newArrayappend = np.append(twoDarray, [[32,33,34,35]],axis=0)
print(newArrayappend)

'''


# Accessing elements in 2 dimensional array
'''
def accessElements(array,rowIndex,columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][columnIndex])

accessElements(twoDarray, 1,2)
'''

# traversal in 2 dimensional array
'''
def traversalTdarray(array):
    for i in range (len(array)):
        for j in range (len(array[0])):
            print(array[i][j])
            
traversalTdarray(twoDarray)
'''

# Searching in two dimensional array
'''
def searchTdarray(array, value):
    for i in range (len(array)):
        for j in range (len(array[0])):
            if (value == array[i][j]):
                return('The value is stored at position'+ str(i)+" "+str(j))
    return("Value not found")

print(searchTdarray(twoDarray, 86))     
'''

# Deletion in 2-Dimensional Array

deleteTdarray = np.delete(twoDarray,0,axis=0)
print(deleteTdarray)