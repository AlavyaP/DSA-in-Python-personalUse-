# Queue with Size Limitation  or fixed Capacity Also know as Circular Queue
class CircularQueue:
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start  = -1
        self.top  = -1
    # to print
    def __str__(self) :
        values = [str(x) for x in self.items] 
        return ' '.join(values)
    

    # to check if the queue is full
    def isFull(self):    #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        if self.top + 1 == self.start :
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize :
            return True
        else:
            return False
        
        
    # is Empty to check if Queue is empty
    def isEmpty(self):     #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        if self.top == -1 :
            return True
        else:
            return False
        
    # enqueue 
    def enqueue(self,value):             #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        if self.isFull():
            return "The Queue is Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1 
                if self.start  == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element has been inserted"
        
    # Dequeue 
    def dequeue(self):                   #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            firstElement = self.items[self.start]
            start =self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize :
                self.start = 0
            else:
                self.start += 1 
            self.items[start] = None
            return firstElement
        
        
        
    # Peek Method 
    def peek(self):             #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items[self.start]
        
        
    # delete method 
    def delete(self):           #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1  
    
                     
        
        
        
        
# code to check the functions 
customQueue = CircularQueue(3)
# print(customQueue.isEmpty())
customQueue.enqueue(5)
customQueue.enqueue(2)
customQueue.enqueue(4)
# print(customQueue)
# customQueue.dequeue()
# print(customQueue.isFull())
# print(customQueue.peek())
customQueue.delete()
print(customQueue)
