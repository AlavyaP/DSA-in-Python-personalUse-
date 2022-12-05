# AVL Tree 
import queueLinkedList as queue
class AVLNode :
    def __init__(self,data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None
        self.height = 1
        
        
        

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

# Searchin in AVL Tree  
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
            
# Helper Function for insertion function
def getHeigh(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeigh(disbalanceNode.leftChild), getHeigh(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeigh(newRoot.leftChild), getHeigh(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeigh(disbalanceNode.leftChild), getHeigh(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeigh(newRoot.leftChild), getHeigh(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeigh(rootNode.leftChild) - getHeigh(rootNode.rightChild)
    
# insert a node in a AVL Tree
def insertNode(rootNode, nodeValue):             # Time Complexity = O(log N) ;; Space Complexity = O(log N) 
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue <rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild,nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild,nodeValue)
        
    rootNode.height = 1 +max(getHeigh(rootNode.leftChild), getHeigh(rootNode.rightChild))
    balance = getBalance(rootNode)
    # left's  condition
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild =leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # right's Condition
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        leftRotate(rootNode)
    return rootNode

# Delete a Node from a AVL Tree

        

 

        
newAVL = AVLNode(5)         # Time Complexity = O(1) ;; Space Complexity = O(1) >> for creating a AVL Tree
newAVL = insertNode(newAVL,10)
newAVL = insertNode(newAVL,15)
newAVL = insertNode(newAVL,20)
levelOrderTraversal(newAVL)