# Graph represention
'''
class Graph:
    def __init__(self,gdict= None):
        if gdict  is None:
            gdict = {}
        self.gdict = gdict 
        
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
        
        
        
# Test Case
customDict = {"a":["b","c"],
              "b":["a","d","e"],
              "c":["a","e"],
              "d":["b","e","f"],
              "e":["d","f"],
              "f":["d","e"]
}
graph = Graph(customDict)
graph.addEdge("e","c")
print(graph.gdict["e"])
'''

class Graph:
    def __init__(self):
        self.adjancency_list = {}
        
        
    def add_vertex(self,vertex):
        if vertex not in self.adjancency_list.keys():
            self.adjancency_list[vertex] = []
            return True
        return False
    
    # helper function to print graph
    def print_graph(self):
        for vertex in self.adjancency_list:
            print(vertex,":",self.adjancency_list[vertex])
    
    
# Test case 
custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.print_graph()