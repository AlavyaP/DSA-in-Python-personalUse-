class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
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

# creating circular doubly linked list

    def createCDLL(self,nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL has been created!"
    
    # Insertion in a circular doubley linked list
    def insertCDLL(self,value,location):
        if self.head is None :
            return "List is Empty"
        else:
            newNode = Node(value)
            if location == 0 :
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1 :
                    tempNode =  tempNode.next
                    index +=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been created Successfully"
        
    # traversal in doubly linked list 
    def traversalCDLL(self):
        if self.head is None :
            print("No node to traverse in this list ")
        else:
            tempNode = self.head
            while tempNode :
                print(tempNode.value)
                if tempNode == self.tail :
                    break
                tempNode = tempNode.next
                
                
    # reverse traversal in CDLL
    def reverseTraversalCDLL(self):
        if self.head is None :
            print("List is Empty")
        else:
            tempNode = self.tail
            while tempNode :
                print(tempNode.value)
                if tempNode == self.head :
                    break
                tempNode = tempNode.prev
                
                
                
    # Searching in a CDLL
    def searchCDLL(self,nodeValue):
        if self.head is None :
            return "The list is empty"
        else:
            tempNode = self.head 
            while tempNode :
                if tempNode.value == nodeValue :
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist"
                tempNode = tempNode.next
                
                
                
    # deletion in circular doubly linked list
    def deleteNode(self,location):
        if self.head is None :
            print("The list is empty")
        else:
            if location == 0 :
                if self.head == self.tail :
                    self.head.prev = None 
                    self.head.next = None 
                    self.head = None
                    self.tail = None 
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1 :
                if self.head == self.tail :
                    self.head.prev = None 
                    self.head.next = None 
                    self.head = None
                    self.tail = None 
                else:
                    self.tail = self.tail.prev 
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curNode = self.head 
                index = 0 
                while index < location - 1 :
                    curNode = curNode.next
                    index +=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print ("The node has been deleted")
            
            
    # deleting the entire list
    def deleteCDLL(self):
        if self.head is None :
            print("List is empty")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode :
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been deleted")
                                
                

                
                    
            
        
                    
                    
            
            
            
        
        








# code for execution of the codes 
circularDLL  = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL ])
# circularDLL.traversalCDLL()
# circularDLL.reverseTraversalCDLL()
# print(circularDLL.searchCDLL(6))
# circularDLL.deleteNode(-1)
circularDLL.deleteCDLL()


print([node.value for node in circularDLL ])