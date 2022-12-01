# tree using LinkedList 
import queueLinkedList as queue
class TreeNode():
    def __init__(self,data) :
        self.data = data 
        self.leftChild = None
        self.rightChild = None
# Time Complexity = O(1) ;; Space Complexity = O(1) >> in creating a tree using linkedList
# newBT = TreeNode("Drinks")
# leftChild = TreeNode("Hot")
# rightChild = TreeNode("Cold")
# newBT.leftChild = leftChild
# newBT.rightChild = rightChild

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


# preorder Traversal
def preOrderTraversal(rootNode):            # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
# preOrderTraversal(newBT)
        
# inOrder Traversal
def inOrderTraversal(rootNode):             # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
# inOrderTraversal(newBT)   


# postOrder Traversal
def postOrderTraversal(rootNode):             # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
# postOrderTraversal(newBT)   

# Level Order Traversal
def levelOrderTraversal(rootNode):          # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

# levelOrderTraversal(newBT)
def searchBT(rootNode,nodeValue):            # Time Complexity = O(N) ;; Space Complexity = O(N)
    if not rootNode:
        return "The Tree is Empty"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"

print(searchBT(newBT,"Cola"))          