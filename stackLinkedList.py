# stack on linked List

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
        
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values) 

 
    # for checking is Empty
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    # push method
    def push (self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
        
    # pop method
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next 
            return nodeValue

    # peek method 
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    # delete method 
    def delete(self):
        self.LinkedList.head = None

# for execution
customStack = Stack()
# print(customStack.isEmpty())
customStack.push(5)
customStack.push(7)
customStack.push(2)
print(customStack)
print("------------")
# print(customStack.pop())
# print(customStack.peek())
print(customStack.delete())

# print(customStack)