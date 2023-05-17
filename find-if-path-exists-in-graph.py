class Unions:
    def __init__(self,n):
        self.rep = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self,k):
        temp = k 
        while self.rep[k] != k:
            k = self.rep[k]
        while self.rep[temp] != temp:
            parent = self.rep[temp]
            self.rep[temp] = k
            temp = parent 
        return k
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if self.size[xrep] > self.size[yrep]:
            self.size[xrep] += self.size[yrep]
            self.rep[yrep] = xrep
        else:
            self.size[yrep] += self.size[xrep]
            self.rep[xrep] = yrep
    def connected(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        return xrep == yrep
class Solution:


    

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        data = Unions(n)
        for x,y in edges:
            data.union(x,y)
        return data.connected(source,destination)