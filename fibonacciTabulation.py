# Fibonacci Series using Tabulation (Bottom Up )

def fibonacciTab(n):  #Time Complexity = O(N) || Space Complexity = O(N)
    tb = [0,1]
    for i in range (2,n+1) :
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]

#  Test Run
print(fibonacciTab(6))