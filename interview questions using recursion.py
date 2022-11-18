# Sum of Digits
''' 
def digitSum(a:int):
    assert a>=0 and int(a)==a,"A positive interger" 
    if a == 0:
        return(0)
    return (a%10+digitSum(int(a//10)))
    
print(digitSum(125))
'''

# Power of a number using recursion
'''
def power(base:int,expo:int):
    assert int(expo) == expo,"A positive Integer"
    if expo ==0:
        return (1)
    elif expo < 0:
        return (1/base*power(base,expo+1))
    return base*power(base,expo-1)

print(power(-4,2))
'''

# Greatest commom divisor
'''
def gcd(a:int,b:int):
    assert int(a) == a and int(b) == b,"Positive integer only"
    if (a<0):
        a = a*-1
    if (b<0):
        b = b*-1
    if b == 0:
        return (a)
    else:
        return gcd(b,a%b)
    
print(gcd(48,18))

'''

# Convert decimal number to binary
'''
def dtb(a:int):
    assert  int(a)==a,"A positive integer please"
    if a ==0:
        return (0)
    else:
        return (a%2+10*dtb(int(a/2)))

print(dtb(13))
'''