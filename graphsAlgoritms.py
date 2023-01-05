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
    
    # Add Vertex
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjancency_list.keys() and vertex2 in self.adjancency_list.keys():
            self.adjancency_list[vertex1].append(vertex2)
            self.adjancency_list[vertex2].append(vertex1)
            return True
        return False
    
    
    # remove Edge 
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adjancency_list.keys() and vertex2 in self.adjancency_list.keys():
            try:
                
                self.adjancency_list[vertex1].remove(vertex2)
                self.adjancency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    
    # Remove Veertex
    def remove_vertex(self,vertex):
        if vertex in self.adjancency_list.keys():
            for other_vertex in self.adjancency_list[vertex]:
                self.adjancency_list[other_vertex].remove(vertex)
            del self.adjancency_list[vertex]
            return True
        return False
    
# Test case 
custom_graph = Graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_edge("A","B")
custom_graph.add_edge("A","C")
custom_graph.add_edge("A","D")
custom_graph.add_edge("B","C")
custom_graph.add_edge("C","D")
custom_graph.print_graph()
print("After Removal")
# custom_graph.remove_edge("A","D")
custom_graph.remove_vertex("A")
custom_graph.print_graph()
