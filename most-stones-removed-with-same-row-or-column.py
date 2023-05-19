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
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = cols = 0
        dic = {}
        c = 0
        for i,j in stones:
            rows = max(rows,i)
            cols = max(cols,j)
        data = Unions(rows + cols + 2)

        for i,j in stones:
            data.union(i,j+rows+1)
            dic[i] = 1
            dic[j+rows+1] = 1
        print(dic)
        for i in dic: 
            if data.find(i) == i:
                c += 1
        return len(stones) - c