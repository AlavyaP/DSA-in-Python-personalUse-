# Coin Change Problem

def coinChange(totalNumber,coins):               # Time Complexity = O(N) & Space Comlexity = O(1)
    N = totalNumber
    coins.sort()
    index = len(coins) -1
    while True :
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1
            
        if N == 0:
            break
        
# run code 
coins = [1,2,5,20,50,100]
coinChange(201, coins)
