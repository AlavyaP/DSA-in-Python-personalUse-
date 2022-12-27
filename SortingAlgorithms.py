import math

# bubble sort 
def bubbleSort(customList):             #Time Complexity = O(N^2) || Space Complexity = O(1)
    for i in range (len(customList)-1):
        for j in range (len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j],customList[j+1] = customList[j+1],customList[j]
                
    print(customList)
    
# Selection Sort 
def selectionSort(customList):               #Time Complexity = O(N^2) || Space Complexity = O(1)
    for i in range (len(customList)):
        min_index = i
        for j in range (i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i],customList[min_index] = customList[min_index], customList[i]
    print(customList)
    
# Insertion Sort 
def insertionSort(customList):     #Time Complexity = O(N^2) || Space Complexity = O(1)
    for i in range (1, len(customList)):
        key = customList[i]
        j = i-1
        while j>=0 and key <= customList[j]:
            customList[j+1] = customList[j]
            j -= 1 
        customList[j+1] = key
        
    # print (customList)  >> this is for the insertSort only, we use return for bucketSort to get the value after sorting the elements from each buckets
    return (customList)

def bucketSort(customList):                 #Time Complexity = O(N^2) || Space Complexity = O(N)
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []
    
    # entering the element is appropriate bucket
    for i in range (numberOfBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberOfBuckets/maxValue)
        arr[index_b-1].append(j)
        
    # for sorting the elemnts in each buckets
    for i in range (numberOfBuckets):
        arr[i] = insertionSort(arr[i])
        
    
    # bring back all the buckets together 
    k = 0
    for i in range (numberOfBuckets):
        for j in range (len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return (customList)


# merge sort  helper function
def merge(customList, l, m, r):
    n1 = m -l + 1 
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range(0,n1):
        L[i] = customList[l+i]
        
    for j in range(0,n2):
        R[j] = customList[m+1+j]  #
        
        # merge this array
        
    i = 0 
    j = 0
    k = l 
    
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j] 
            j += 1
        k += 1
        
        
    while i < n1 :
        customList[k] = L[i]
        i += 1
        k += 1
        
    while j < n2 :
        customList[k] = R[j]
        j += 1
        k += 1
        
# Merge Sort 
def mergeSort(customList, l, r):            #Time Complexity = O(NLogN) || Space Complexity = O(N)
    # calling them recursively
    if l < r :
        m = (l + (r-1))//2
        mergeSort(customList,l,m)
        mergeSort(customList,m+1,r)
        merge(customList,l,m,r)
    return customList
        
         
            
            
    
# test run
cList = [9,8,7,6,5,4,3,2,1]
# bubbleSort(cList)
# selectionSort(cList)
# insertionSort(cList)
# print(bucketSort(cList))
print(mergeSort(cList,0,8))