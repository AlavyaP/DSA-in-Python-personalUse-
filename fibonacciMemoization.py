# Fibonacci Series in Dynamic Programing using Top Down with Memoization

def fibMemo(n,memo):            #Time Complexity = O(N)  || Space Complexity = O(N)
    if n==1 :
        return 0
    if n ==2 :
        return 1
    if not n in memo :
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo) 
    return memo[n]


#  Test Run 
myDict = {}
print(fibMemo(6, myDict))