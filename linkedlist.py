# Linked List
# creating single linked list
class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
# Insertion in a Linked List

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if (location == 0):
                newNode.next = self.head
                self.head = newNode
            elif (location == -1):
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while (index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if (tempNode == self.tail):
                    self.tail = newNode

    # Traverse In a Linked List
    def traverseSLL(self):
        if (self.head == None):
            print("The Singly Linked List does not exits")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search in a linked list
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("List is Empty")
        else:
            node = self.head
            while node is not None:
                if (node.value == nodeValue):
                    return nodeValue
                node = node.next
            return ("The node does not Exist")

    # Deletion in a Linked List
    def deleteSLL(self, location):
        if self.head is None:
            print("The list is Empty")
        else:
            if (location == 0):   # in this we are deleting the first node

                if (self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif (location == -1):  # in this we are deleting the last node
                if (self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None :
                        if( node.next == self.tail):
                            break
                        node = node.next
                        self.tail = None
            else:  #deletion from any node of the linked  list
                tempNode = self.head
                index = 0
                while (index < location -1):
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
                
    # delete the entire linked list
    def deleteEntireSLL(self):
        if self.head is None :
            print("NO List")
        else:
            self.head = None
            self.tail = None   
        
         
# Exceution Code are Below
signlyLinkedList = SLinkedList()
signlyLinkedList.insertSLL(1, 1)
signlyLinkedList.insertSLL(2, 1)
signlyLinkedList.insertSLL(3, 1)
signlyLinkedList.insertSLL(4, 1)
signlyLinkedList.insertSLL(5, -1)
'''
node1= Node(1)
node2= Node(2)

signlyLinkedList.head = node1
signlyLinkedList.head.next  = node2
signlyLinkedList.tail  = node2

'''
print([node.value for node in signlyLinkedList])
# signlyLinkedList.traverseSLL()
# print(signlyLinkedList.searchSLL(5))
# signlyLinkedList.deleteSLL(2)
signlyLinkedList.deleteEntireSLL()

print([node.value for node in signlyLinkedList])

