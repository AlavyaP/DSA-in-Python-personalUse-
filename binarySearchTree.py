# Binary Search Tree Using Linked List

# import queueLinkedList
import queueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None



# inserting to the node of the tree
def insertNode(rootNode, nodeValue):            # Time Complexity = O(log N) ;; Space Complexity = O(log N) 
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been Successfully Inserted"


# PreOrder Traversal 
def preOrderTraversal(rootNode):        # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
# InOrder Traversal 
def inOrderTraversal(rootNode):           # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
# Post Order Traversal 
def postOrderTravesal(rootNode):            # Time Complexity = O(N) ;; Space Complexity = O(N) 
    if not rootNode:
        return
    postOrderTravesal(rootNode.leftChild)
    postOrderTravesal(rootNode.rightChild)
    print(rootNode.data)
    
    
# Level Order Traversal
def levelOrderTraversal(rootNode):     # we use Queue for level order traversal 
    # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
                
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# Searching in a Binary Search Tree
def searchNode(rootnode,nodeValue):         # Time Complexity = O(log N) ;; Space Complexity = O(log N)
    if rootnode.data == nodeValue:
        print("The Value is Found")
    elif nodeValue < rootnode.data:
        if rootnode.leftChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchNode(rootnode.leftChild,nodeValue)        
    else:
        if rootnode.rightChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchNode(rootnode.rightChild,nodeValue) 

# find the min node of the tree
def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current
    
# Delete A Node in Binary Tree
def deleteNode(rootNode,nodeValue):         # Time Complexity = O(log N) ;; Space Complexity = O(log N)
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data :
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data :
        rootNode.rightNode = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode =  None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode =  None
            return temp
        # delete if node has 2 children
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

# Delete Entire Tree
def deleteBST(rootNode):            # Time Complexity = O(1) ;; Space Complexity = O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The Tree Has Been Deleted"


    

# To run the above code
newBST = BSTNode(None)          # Time Complexity = O(1) ;; Space Complexity = O(1) >> for creating a binarySearchTree
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
print(newBST.data)
print(newBST.leftChild.data)
preOrderTraversal(newBST)
inOrderTraversal(newBST)
postOrderTravesal(newBST)
searchNode(newBST,101)
deleteNode(newBST,100)
print(deleteBST(newBST))
levelOrderTraversal(newBST)