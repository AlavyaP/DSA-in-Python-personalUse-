# this is a stack with size limit 
class Stack:
    def __init__(self,maxSize) -> int:
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    
    # for checking if the stack is empty or not
    def isEmpty(self):
        if self.list == [] :
            return True
        else: 
            return False
        
    
    # function to check if the stack is full or not 
    def isFull(self):
        if len(self.list) == self.maxSize :
            return True
        else:
            return False
        
        
    # push method to insert a element in a stack
    def push(self,value):
        if self.isFull():
            return "The Stack is Full"
        else:
            self.list.append(value)
            return "The element has been Inserted Succesfully"
    
    # pop method to remove the element from the stack
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            self.list.pop()
            
    # peek method to show the top element    
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
           return self.list[len(self.list) - 1]
       
       
    # delete the Entire Stack
    def delete(self):
        self.list = None
        
        
        
# code to test the above operations
customStack = Stack(5)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(7)
customStack.push(5)
customStack.push(1)
# customStack.pop()
# print(customStack.peek())
customStack.delete()

print(customStack)