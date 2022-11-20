# Question 1 -->> How to find the missing number in an integer array of 1 to 100?
# my list for example
'''
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def missingNumber(list,n): 
   sum1 = sum(list)
   sum2 = 100*101/2
   print(sum2-sum1)

missingNumber(mylist,100)

'''

# Question2 -->> Write a program to find all pairs of integers whose sum is equal to a given number?.
'''
def findPair(nums,target):
    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif ((nums[i]+nums[j]) == target):
                print(i, j)          
                
my_num = [1,2,3,2,3,4,5,6]
findPair(my_num,6)
'''
   
# Question 3 -->> How to check if an array contains a number in Python?  
'''
import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
def linearSearch(arr,find):
    for i in range (len(arr)):
        if arr[i] == find:
            print(i)
        
linearSearch(myArray,7)

'''

# Question 4  --> How to find maximum product of two integers in the array where all elements are positive?
'''
import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])

def findMaxProduct(arr):
    max_Product = 0
    for i in range (len(arr)):
        for j in range (i+1,len(arr)):
            if (arr[i] *arr[j])> max_Product:
                max_Product = arr[i]*arr[j]
                pairs = str(arr[i]) +","+ str(arr[j])
    print(pairs)        
    print(max_Product)        
    
    
findMaxProduct(myArray)
'''


# Question 5 --> Is Unique: Implement an algorithm to determine if a list has all unique characters, using python list.?

'''
myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def isUnique(list):
    notUnique = []
    for i in list:
        if i in notUnique:
            print(i)
        else:
            notUnique.append(i)
    return True   
isUnique(myList)
'''

# Question 6 --> Check if one is permutation of other string
'''
list1= [1,2,3]
list2 = [1,3,2]
def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()    
    list2.sort()
    if (list1 == list2):
        return True
    else:
        return False    
    
print(permutation(list1,list2))
'''

# Question 7 --> Rotate Matrix - Given an image represented by an NxN matrix write a method to rotate the image by 90 degrees.?
'''
import numpy as np

myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])

def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range (n//2):
        first = layer
        last = n- layer - 1
        for i in range (first,last):
            # save the top element
            top = matrix[layer][i]
            # for the left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # for the bottom to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # for right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top  to right 
            matrix[i][-layer-1] = top
    return(matrix)

print(rotateMatrix(myArray))    

'''