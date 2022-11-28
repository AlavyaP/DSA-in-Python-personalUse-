# Queue Using Python List
class Queue:
    def __init__(self):
        self.items = [] 
        
    # print function    
    def __str__(self) -> str:
        values = [str(x) for x in self.items] 
        return ' '.join(values)
    
    
    # for checking if queue is empty
    def isEmpty(self):   #time and space Complexity  == O(1)
        if self.items == [] or self.items is None: 
            return True
        else:
            return False
        
    # insertion in the queue >> enqueue
    def enqueue(self,value):    #time and space Complexity  == O(N) worst time complexity = O(n^2)
        self.items.append(value)
        return "The item has been Inserted at the end of the queue"
    
    # removal is the queue >> dequeue   
    def dequeue(self):     #TimeComplexity = O(N)  ;Space Complexity  = O(1)
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items.pop(0)
        

    # to display the first element of the queue >> Peek Method
    def peek(self):      #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        if self.isEmpty():
            return "The Queue is empty"
        else:
            return self.items[0]
        

    # deletion of the entire queue
    def delete(self):     #TimeComplexity = O(1)  ;Space Complexity  = O(1)
        self.items = None
        
           
    
    

# code to test the function
customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(5)
customQueue.enqueue(4)

# print(customQueue.peek())
customQueue.delete()

# print(customQueue)