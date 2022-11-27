# creation of stack using without size limit 
class Stack(): 
    def __init__(self) -> None:
        self.list = []
        
        
    def __str__(self,):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # for checking the is Empty parameter
    def isEmpty(self):
        if self.list == [] :
            return True
        else:
            return False
        
        
    # for push method in stack
    def push(self,value):
        self.list.append(value)
        return "The Element has been Successfully Inserted"
    
    # pop method for a stack
    def pop(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.list.pop()
        
        
    # peek method in Stack
    def peek(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list[len(self.list) - 1]
    # to delete the entire list 
    def delete(self):
        self.list = None
        
        
        
        
        
        
        
# code for running the above operators
customStack = Stack()
# print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(5)
# customStack.pop()
# print(customStack.peek())
customStack.delete()
print(customStack)
