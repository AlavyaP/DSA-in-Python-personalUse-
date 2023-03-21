# Find the longest Planidromic Subsequence

# Palindrome  is a string that reads the same from backward as well as front

def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2  + findLPS(s, startIndex +1 , endIndex -1)
    
    else:
        op1 =  findLPS(s, startIndex, endIndex -1)        
        op2 =  findLPS(s, startIndex +1 , endIndex)    
        return max (op1, op2)
    
    
    
# Test Run    
print(findLPS("ELRMENMET", 0, 8))