# print("Hello World")
# Question == Russian Doll 

# Solution
'''
doll = int(input())
if (doll == 1):
    print("All Dolls are Opened")
else:
    while (doll>0):
        a = doll-1
        print(a)
        doll =a 
        
'''

# Factorial using recursive method
'''
def factorial (a:int):
    assert a>=0 and int(a)==a , "Enter a positive integer"
    if a in [0,1]:
        return (1)
    else:
        return (a * factorial(a-1))  
    
print(factorial(4.5))

'''
# fibonacci Series
def fibonacci (n :int):
    assert n>=0 and int(n) == n, "Enter a positive integer"
    if n in [0,1]:
        return (n)
    else:
        return (fibonacci(n-1)+ fibonacci(n-2))
      
print(fibonacci(7))