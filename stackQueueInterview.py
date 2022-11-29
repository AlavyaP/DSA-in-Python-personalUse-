# Question 1 -->> Describe how you could use  single Python List to implement Three Stack 
# '''
class MultiStack:
    def __init__(self,stacksize):
        self.numberstacks = 3
        self.custList =  [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    
    # to check if the stack is full
    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stacksize :
            return True
        else:
            return False
    # to check if the stack is empty 
    def isEmpty(self,stacknum):
        if self.sizes[stacknum] == 0 :
            return True
        else:
            return False
        
        
    # helper method 
    def indexOfTop(self,stacknum):
        offset =stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    
    # enter a elemement in stack
    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] =item
            
    # remove the element for the stack
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
        
    # to show the first element
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value
        
        
# code to execute the above function
customStack = MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(5,0)
customStack.push(2,0)
customStack.push(4,2)
print(customStack.pop(0))
print(customStack.peek(1))

            
            

# '''