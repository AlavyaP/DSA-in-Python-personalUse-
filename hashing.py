# this is for hashing 
# this is kind of a algorithm instead of data structure
# hashing for integers values  
def mod(number,cellnumber):
    return (number%cellnumber)

# hashing for ASCII functions -->> Strings
def modASCII(string,cellnumber):
    total = 0 
    for i in string:
        total += ord(i)
    return (total % cellnumber)


print(modASCII)
print(mod)


'''
this is a sudo code just for understanding how hashing works, but hashing is much complex in real word
This is just a basic for undsertanding
'''