# Queue using a singly linked list 

class Node :
    def __init__ (self,value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        curNode = self.head
        while curNode :
            yield curNode
            curNode = curNode.next 
            
            
class Queue:                # Time Complexity = O(1) ;; Space Complexity = O(1)
    
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values) 
    
    
      # isEmpty Method to check if the queue is empty
    def isEmpty(self):              # Time Complexity = O(1) ;; Space Complexity = O(1)
        if self.linkedList.head == None :
            return True 
        else: 
            return False 
        
    
    def enqueue(self,value):            # Time Complexity = O(1) ;; Space Complexity = O(1)
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
            

    # dequeue method to remove the first element of the queue 
    def dequeue(self):                   # Time Complexity = O(1) ;; Space Complexity = O(1)
        if self.isEmpty():
            return "The Queue is empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail :
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next 
            return tempNode
            
            
    # peek method >> returns the first element
    def peek(self):                    # Time Complexity = O(1) ;; Space Complexity = O(1)
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.linkedList.head
        
    
    # delete method 
    def delete(self):                   # Time Complexity = O(1) ;; Space Complexity = O(1)
        self.linkedList.head = None
        self.linkedList.tail = None
            
  
            
            
            
            

# code to test our above program
customQueue = Queue()
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(4)
# print(customQueue)
# print(customQueue.isEmpty())
# print(customQueue.dequeue())
# print(customQueue.peek())
# print(customQueue)
