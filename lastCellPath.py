# It is similar to min Cost but here we have to reach  the end matrix  with given "Total Cost"

def numberOfPaths(twoDArray,row ,col, cost):
    if cost < 0 :
        return 0
    elif row == 0 and col == 0 :
        if twoDArray [0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0 :
        return numberOfPaths(twoDArray,0, col-1, cost - twoDArray[row][col])
    
    elif col == 0 :
        return numberOfPaths(twoDArray,row -1, 0, cost - twoDArray[row][col])
    
    else:
        op1 = numberOfPaths(twoDArray,row -1, col, cost - twoDArray[row][col])
        op2 = numberOfPaths(twoDArray, row, col-1, cost - twoDArray[row][col])
        return op1 + op2
        
# Test Run

TwoDList = [[4,7,1,6],
            [5,7,3,9],
            [3,2,1,2],
            [7,1,6,3]
            ]

print (numberOfPaths(TwoDList,3,3,25))