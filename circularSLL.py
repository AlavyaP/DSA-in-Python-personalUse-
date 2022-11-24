# Circular Singly Linked List
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break 
            
            
            
    # Creating a Circular Linked List

    def createCSLL(self,nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return ("The CSLL has been created")
    
    
    # Insertion in a Circular Linked List
    
    def insertCSLL(self,value,location):
        if self.head is None:
            return "The Head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode 
            return "The node was successfully Inserted"     
        
        
    # Traversing in a Linked List
    def traversalCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode ==self.tail.next:
                    break
                
                
                
    # Searching in a Circular Linked List
    def searchCSLL(self,nodeValue):
        if self.head is None:
            return "It is Empty"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode =  tempNode.next
                if tempNode == self.tail.next:
                    return "The node is not available in the CSLL"
                
                
    # Deletion is   a Circular Linked List
    def deleteNode(self,location):
        if self.head is None :
            print("There is not any node in CSLL")
        else: 
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
                    
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode  = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    # Delete the entire CSLL
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
                        
                
                               
                
                
                
        
    
    
    # execution code
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(2,2)
# circularSLL.traversalCSLL()
# print(circularSLL.searchCSLL(4))
print([node.value for node in circularSLL])
# circularSLL.deleteNode(1)
circularSLL.deleteEntireCSLL()

print([node.value for node in circularSLL])








