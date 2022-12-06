# Implementation of binary Heap using Array
class Heap():
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
        
# peek of Heap Method 
def peekofHeap(rootNode):           #Time Complexity = O(1) && Space Complexity = O(1) 
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]

# Size of Heap 
def sizeOfHeap(rootNode):       #Time Complexity = O(1) && Space Complexity = O(1) 
    if not rootNode:
        return 
    else:
        return rootNode.heapSize
    
    
# level order Traversal
def levelOrderTraversal(rootNode):           #Time Complexity = O(N) && Space Complexity = O(1) 
    if not rootNode:
        return
    else:
        for i in range (1,rootNode.heapSize+1):
            print(rootNode.customList[i])
            
# heapify >> to move element in the array
def heapifyTreeInsert(rootNode, index, heapType):       #Time Complexity = O(log N) && Space Complexity = O(log N)
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex] :
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode,parentIndex,heapType)
    
    if heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
    heapifyTreeInsert(rootNode,parentIndex,heapType)
    
# insert Method
def insertNode(rootNode,nodeValue,heapType):            #Time Complexity = O(log N) && Space Complexity = O(log N)
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Heap is Full"
    rootNode.customList[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize  += 1
    heapifyTreeInsert (rootNode, rootNode.heapSize,heapType)
    return "The value has been Inserted"


# Extract an Element in a heap
def heapifyTreeExtract(rootNode,index, heapType):
    leftIndex =index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    
    if rootNode.heapSize < leftIndex :
        return
    elif rootNode.heapSize == leftIndex :
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp    
            return
    # if we have 2 children
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index]  > rootNode.customList[swapChild]:
                temp = rootNode.customIndex[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
                
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
                
        heapifyTreeExtract(rootNode,swapChild,heapType)
        
# Extract Method
def extractNode (rootNode,heapType):         #Time Complexity = O(Log N) && Space Complexity = O(log N)
    if rootNode.heapSize == 0:
        return
    else:
        extractNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1 
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractNode
# Delete a Entire Binary Heap
def deleteEntireBP(rootNode):       #Time Complexity = O(1) && Space Complexity = O(1)
    rootNode.customList = None

            
         
        
newHeap = Heap(5)  #Time Complexity = O(1) && Space Complexity = O(N)  >> Creating a Heap
# print(sizeOfHeap(newHeap))
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")
# print(extractNode(newHeap,"Max"))
# extractNode(newHeap,"Max")
deleteEntireBP(newHeap)
levelOrderTraversal(newHeap)
