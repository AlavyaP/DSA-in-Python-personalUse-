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
        
# Quick Sort helper function
def swap(my_list,index1,index2):
    # temp = my_list[index1]
    # my_list[index1] = my_list[index2]
    # my_list[index2] = temp >> the same is done in below code 
    my_list[index1],my_list[index2] = my_list[index2],  my_list[index1] 
    
    
def pivot(my_list,pivot_index,end_index):
    swap_index = pivot_index
    for i in range (pivot_index+1,end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index +=1
            swap(my_list,swap_index,i)
    swap(my_list,pivot_index,swap_index)
    return swap_index


# Quick Sort 
def quickSort_helper(my_list,left,right):
    if left < right:
        pivot_index = pivot(my_list, left,right)
        quickSort_helper(my_list,left,pivot_index -1)
        quickSort_helper(my_list,pivot_index+1,right)
    return my_list

def quickSort(my_list):    #Time Complexity = O(NLogN) || Space Complexity = O(N)
    return quickSort_helper(my_list,0,len(my_list)-1)
        
# test run for pivot and swap 
my_list = [3,5,0,6,2,1,4]
# print(pivot(my_list,0,6))
# print(my_list)
# print(quickSort(my_list))


# Heap Sort
# Heapify method
def heapify(customList,n,i):
    smallest = i
    l = 2*i +1
    r = 2*i +2
    if l < n and customList[l] < customList[smallest] :
        smallest = l
    # For right side of tree     
    if r < n and customList[r] < customList[smallest] :
        smallest = r
        
    if smallest != i :
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList,n,smallest)    
        
# heap Sort      
def heapSort(customList):            #Time Complexity = O(NLogN) || Space Complexity = O(1)
    n = len(customList)
    for i in range (int(n/2)-1,-1,-1):
        heapify(customList,n,i)
    for i in range (n-1,0,-1):
        customList[i],customList[0] = customList[0],customList[i]         
        heapify(customList,i,0)
    customList.reverse()      
    
# test run
cList = [9,8,7,6,5,4,3,2,1]
# bubbleSort(cList)
# selectionSort(cList)
# insertionSort(cList)
# print(bucketSort(cList))
# print(mergeSort(cList,0,8))
heapSort(cList)
print(cList)