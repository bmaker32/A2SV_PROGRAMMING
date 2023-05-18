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
        if xrep < yrep:
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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ans = []
        data = Unions(26)
        for i in range(len(s1)):
            st = ord(s1[i])-97
            st2 = ord(s2[i])-97
            data.union(st,st2)
        for i in range(len(baseStr)):
            st = ord(baseStr[i])-97
            num = data.find(st)
            ans.append(chr(num+97))
            print(num,ans)
        return "".join(ans)