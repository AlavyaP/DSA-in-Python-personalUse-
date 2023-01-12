# Floyd Warshall Algorithm in python

INF = 9999  #variable INF whose value is 9999 and is a infinity
# Printing the solution
def printSolution(nV, distance): #nV = nuber of vertices
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


# FW algorithm
def floydWarshall(nV,G):            #Time Complexity = O[V^3] && Space Complexity = O[V^2]
    distance = G
    for k in range (nV):
        for i in range (nV):
            for j in range (nV):
                distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])
                
                
    printSolution(nV,distance)
                
            
# Test Run

G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

floydWarshall(4, G)

