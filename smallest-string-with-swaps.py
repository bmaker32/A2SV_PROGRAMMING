class Unions:  
    def __init__(self,n):
        self.rep = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self,k):
        temp = k 
        while self.rep[k] != k:
            k = self.rep[k]
        return k
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep > yrep:
            self.size[xrep] += self.size[yrep]
            self.rep[yrep] = xrep
        else:
            self.size[yrep] += self.size[xrep]
            self.rep[xrep] = yrep
    def connected(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        return xrep == yrep

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        N = len(s)
        
        uf = Unions(N)
        for edge in pairs:
            uf.union(*edge)
            
        connected_stacks = collections.defaultdict(list)  
        for i in range(N):
            connected_stacks[uf.find(i)].append(s[i])
        
        for stack in connected_stacks.values():
            stack.sort(reverse=True)   
            
        new = "".join([connected_stacks[uf.find(i)].pop() for i in range(N)])
        
        return new