# -----------------------------------------------------------------------------------------------------------------------
# importing linked list 
from LinkedListInterview import LinkedList,Node
# Interview questions  related to Linked List 
# -------------------------------------------------------------------------------------------------------------------
# Question 1 -->> Write a Code to remove the duplicates from a unsorted linked list >> Remove Duplicate
'''


# using temporary buffer 

def removeDups(ll):
    if ll.head is None :
        return
    else :
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next :
            if currentNode.next.value in visited :
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll
    
    
    
    # if the question says the we can't use linked list

def removeDups1(ll):
    if ll.head is None :
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next :
            if runner.next.value == currentNode.value :
                runner.next = runner.next.next
            else:
                runner = runner.next 
        currentNode = currentNode.next
    return ll.head
            
customLL = LinkedList()
customLL.generate(10,0,19)
print(customLL)
removeDups1(customLL)
# removeDups(customLL)
print(customLL)
'''
# Question 2 : >> Implement  and algorithm to find the nth last term to the last element of a singly linked list?
'''
def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    
    for i in range (n):
        if pointer2 is None :
            return None
        pointer2 = pointer2.next
    
    while pointer2 :
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


# testing the code 
customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(nthToLast(customLL,3))
'''


# Question 3 >> Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.?
'''
def partition(ll,x):
    curNode = ll.head
    ll.tail = ll.head
    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x :
            curNode.next = ll.head
            ll.head = curNode 
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
        
    if ll.tail .next is not None :
        ll.tail.next = None
        
customLL = LinkedList()
customLL.generate(10,0,20)
print(customLL)
partition(customLL,10)
print(customLL)
'''

# Question 4 >> You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
'''
def sumList(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    
    while n1 or n2 :
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2: 
            result += n2.value
            n2 = n2.next 
        ll.add(int(result % 10))
        carry = result / 10
        
    return ll
    

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print(llA)
print(llB)
print(sumList(llA, llB))
'''

# Question 5 >>Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth node of
# the first linked list is the exact same node (by reference) as the jth node of the second linked
# list, then they are intersecting.
# '''
def intersection(llA,llB):
    if llA.tail is not llB.tail :
        return False 
    
    lenA = len(llA)
    lenB = len(llB)
    
    shorter = llA if lenA < lenB else llB 
    longer = llB if lenA < lenB else llA 
    
    diff = len(longer) - len(shorter) 
    longerNode = longer.head
    shorterNode = shorter.head
    
    for i in range (diff):
        longerNode = longerNode.next 
        
    while shorterNode is not longerNode :
        shorterNode = shorterNode.next 
        longerNode = longerNode.next 
        
    return longerNode


# creating a additional add function
def addSameNode(llA,llB,value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode 
    
    
    # to execute the code 
    
llA = LinkedList()
llA.generate(3,0,10)
# llb
llB = LinkedList()
llB.generate(4,0,10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,14)

print(llA)
print(llB)

# checking the intersection function
print(intersection(llA,llB))
# '''

    
