# Dis Joint Set in Python
class DisjointSet :                 #Time Complexity = O() || Space Complexity = O()
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices,0)
        
    # findset
    def find(self,item):
        if self.parent[item] == item :
            return item
        else:
            return self.find(self.parent[item])
        
        
        
    # unionSet method
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = [yroot]
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = [xroot]
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
            

# test run 
vertices = ["A","B","C","D","E"]
ds = DisjointSet(vertices)
ds.union("A","B")
print(ds.find("A"))    