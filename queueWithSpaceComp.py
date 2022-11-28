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
        
        
        
        
# code to check the functions 
customQueue = CircularQueue(3)
# print(customQueue.isEmpty())
print(customQueue.isFull())