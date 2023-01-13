# Graph Traversal 

class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict 
    
    def addEdge (self,vertex,edge):
        self.gdict[vertex].append(edge)
        
    # BFS   
    def bfs(self,vertex):             #Time Complexity = O[V^2] && Space Complexity = O[E]
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)  # i miss this line thats why it went to endless loop
                    queue.append(adjacentVertex)
                    
                    
    #DFS   
    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
                    
# Test RUN 
customDict = {"a" : ["b","c"],
              "b" : ["a","d","e"],
              "c" : ["a","e"],
              "d" : ["b","e","f"],
              "e" : ["d","f"],
              "f" : ["d","e"]
              }

graph = Graph(customDict)
# graph.bfs("a")
graph.dfs("a")