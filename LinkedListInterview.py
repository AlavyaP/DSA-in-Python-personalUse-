# linked list for the interview questions 
from random import randint


class Node :
    def __init__(self,value = None) -> int:
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self) -> str:
        return str(self.value)
    
class LinkedList:
    def __init__(self,value = None):   
        self.head = None
        self.tail = None
        
    def __iter__(self):
        curNode = self.head
        while curNode :
            yield curNode
            curNode = curNode.next
    
    def __str__(self) -> str:
        values = [str(x.value) for x in self]
        return '->'.join(values)
    
    
    # to count the element in a list 
    def  __len__(self):
        result = 0
        node = self.head
        while node :
            result +=1 
            node = node.next
        return result 
    
    
    # addition function in a linked list
    def add (self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    # generate a linked list with random values
    def generate (self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for i in range (n):
            self.add(randint(min_value,max_value))
        return self
        
    

# code for execution of the above code 
# customLL = LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# print(len(customLL))
        
            
             
            