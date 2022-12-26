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
        
    print(customList)
            
            
    
# test run
cList = [9,8,7,6,5,4,3,2,1]
# bubbleSort(cList)
# selectionSort(cList)
insertionSort(cList)