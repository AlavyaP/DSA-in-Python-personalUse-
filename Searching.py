# Linear Search
def linearSearch(array,value):  # Time Complexity = O(N) && Space Complexity = O(1)
    for i in range (len(array)):
        if array[i] == value :
            return i 
    return -1
    
# print(linearSearch([20,30,40,50,90],50))

# Binary Search
import math
def binarySearch(array,value):          #Time Complexity = O(logN) && Space Complexity = O(1)
    start = 0
    end = len(array) -1 
    middle = math.floor((start+end)/2)
    while not (array[middle] == value) and start <=end:
        if value < array[middle]:
            end = middle -1 
        else:
            start = middle + 1
        middle = math.floor((start+end)/2)
        print(start,middle,end)
    if array[middle] == value:
        return middle
    else :
        return -1
    
    
custArray = [8,9,12,15,17,19,20,21,28]
binarySearch(custArray,69) 