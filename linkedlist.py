# Linked List
# creating single linked list
class Node:
    def __init__(self,value=None) -> None:
        self.value = value
        self.next = None
    
class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
signlyLinkedList = SLinkedList()
node1= Node(1)
node2= Node(2)

signlyLinkedList.head = node1
signlyLinkedList.head.next  = node2
signlyLinkedList.tail  = node2

# '''
# Insertion in a Linked List
