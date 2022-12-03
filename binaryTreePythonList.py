# Tree Using Python List


class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size 
        
    # insert in a binary Tree
    def insertNode(self,value):              # Time Complexity = O(1) ;; Space Complexity = O(1)
        if self.lastUsedIndex + 1 ==self.maxSize:
            return "The Tree is Full"
        self.customList[self.lastUsedIndex + 1 ]  = value
        self.lastUsedIndex +=1 
        return "The value has been inserted"
    

    # serach method for a binary tree    
    def searchNode(self,nodeValue):              # Time Complexity = O(N) ;; Space Complexity = O(1)
        for i in range (len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found" 
    
    
# PreOrder Traversal
    def preOrderTraversal(self,index):               # Time Complexity = O(N) ;; Space Complexity = O(N)
        if index > self.lastUsedIndex :
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)
# InOrder Traversal
    def inOrderTraversal(self,index):               # Time Complexity = O(N) ;; Space Complexity = O(N)
        if index > self.lastUsedIndex :
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)
        
# PostOrder Traversal
    def postOrderTraversal(self,index):               # Time Complexity = O(N) ;; Space Complexity = O(N)
        if index > self.lastUsedIndex :
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])
        
        
# level Order traversal
    def levelOrderTraversal(self, index):             # Time Complexity = O(N) ;; Space Complexity = O(N)
        for i in range (index,self.lastUsedIndex +1):
            print(self.customList[i])
            
            
# Delete a node from a binary Tree
    def deleteNode(self,value):                 # Time Complexity = O(N) ;; Space Complexity = O(1)
        if self.lastUsedIndex == 0:
            return "There is no Node to delete"
        for i in range (1,self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]  = None
                self.lastUsedIndex -= 1
                return "The Node has been Deleted"
            
            
# Delete Entire Tree
    def deleteBT(self):  # Time Complexity = O(1) ;; Space Complexity = O(1)
        self.customList = None
        return "The Binary Tree Has Been Deleted Successfully"
        
            
    
        
        
        
newBT = BinaryTree(8)  #>> creation of a tree in python list           # Time Complexity = O(1) ;; Space Complexity = O(N)      
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
# print(newBT.searchNode("Cold"))
# newBT.preOrderTraversal(1)
# newBT.inOrderTraversal(1)
# newBT.postOrderTraversal(1)
newBT.levelOrderTraversal(1)
# print(newBT.deleteNode("Hot"))
# print(newBT.deleteBT())

# newBT.levelOrderTraversal(1)

