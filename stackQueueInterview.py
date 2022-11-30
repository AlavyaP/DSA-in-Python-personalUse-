# Question 1 -->> Describe how you could use  single Python List to implement Three Stack 
'''
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
'''


# Question 2 >> How would you design a stack which, in addition to push and pop, has a function min which 
# returns the minimum element? Push, pop and min should all operate in O(1).
'''
class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    
    # print method 
    def __str__(self):
        string = str(self.value)
        if self.next:
            str += ',' +str(self.next)
        return string
    
class Stack():
    def __init__(self) -> None:
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    
    # push method 
    def push(self,item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node (value = self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node (value= item, next= self.minNode)
        self.top = Node (value= item,next= self.top)
        
        
    # pop method
    def pop(self):
        if not self.top :
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.value
        return item
    
# code to execute the code 
customStack = Stack()
customStack.push(5)
# print(customStack.min())
# customStack.push(2)
customStack.push(4)
customStack.push(3)
customStack.pop()
print(customStack.min())
'''

# Question 3 >> Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real
# life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of
# several stacks and should create a new stack once the previous one exceeds capacity,
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is,
# pop() should return the same values as it would if there were just a single stack).

# Follow Up: Implement a function popAt (int index) which performs a pop operation on a specific sub – stack.
'''
class PlateStack():
    def __init__(self,capacity):
        self.capacity = capacity    
        self.stacks = []
    def __str__(self):
        return self.stacks
    
    # push method
    def push(self,item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity :
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
            
    # pop method 
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0 :
            self.stacks.pop()
        if len (self.stacks) == 0 :
            return None
        else:
            return self.stacks[-1].pop()
        
    # method to pop at a particular stack 
    def pop_at(self,stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None
# code to execute the above methods
customStack = PlateStack(2) 
customStack.push(2)
customStack.push(1)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(0))
'''

# Question 4 >> Implement Queue class which implements a queue using two stacks.
'''
class Stack():
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)
    def push(self,item):
        self.list.append(item)
    def pop(self):
        if len(self.list) == 0:
            return None 
        return self.list.pop()
    
class QueueviaStack():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    def enqueue(self,item):
        self.inStack.push(item)
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop() 
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result
    
# code to execute the above method 
customQueue = QueueviaStack()
customQueue.enqueue (1)
customQueue.enqueue (2)
customQueue.enqueue (3)
print(customQueue.dequeue())    
customQueue.enqueue (4)
print(customQueue.dequeue())    
'''

# Question 5 >> An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out"
# basis. People must adopt either the "oldest" (based on arrival time) of all animals at the
# shelter, or they can select whether they would prefer a dog or a cat (and will receive the
# oldest animal of that type). They cannot select which specific animal they would like. Create
# the data structures to maintain this system and implement operations such as enqueue,
# dequeueAny, dequeueDog, and dequeueCat.

# '''
class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []
        
    # to enter a animal
    def enqueue(self,animal,type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
            
    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog 
    
    def dequeueAny(self):
        if len(self.cats) == 0 :
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result
    
# code to execute the above methods
customQueue = AnimalShelter()
customQueue.enqueue('Cat1','Cat') 
customQueue.enqueue('Cat2','Cat') 
customQueue.enqueue('Dog1','Dog') 
customQueue.enqueue('Cat3','Cat') 
customQueue.enqueue('Dog2','Dog')
print(customQueue.dequeueAny()) 
        
            
# '''