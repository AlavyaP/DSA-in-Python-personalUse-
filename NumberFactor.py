# it is a question that uses divide and conquere 

def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n ==3 :
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1 + subP2 + subP3
    
    
# test code 
print(numberFactor(5))