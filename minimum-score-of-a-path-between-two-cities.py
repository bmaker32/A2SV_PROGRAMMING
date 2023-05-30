class UnionSet:
    def __init__(self,size):
        self.mini = {i:float('inf') for i in range(size)}
        self.rep = {i:i for i in range(size)}
        
        self.size = {i:1 for i in range(size)}

    def find(self,num):
        root = num
        while root != self.rep[root]:
            root = self.rep[root]
        
        while num != self.rep[num]:
            parent = self.rep[num]
            self.rep[num] = root
            num = parent
        
        return root

    def union(self,num1,num2,num3):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        

        if self.size[rep1] > self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            # print(self.mini,"and",self.size)
            self.mini[rep1] = min(self.mini[rep1],num3,self.mini[rep2])
            self.rep[rep2] = rep1
        else:
            self.size[rep2] += self.size[rep1]
            self.mini[rep2] = min(self.mini[rep2],num3,self.mini[rep1])
            self.rep[rep1] = rep2
    
    def onSamePath(self,num1,num2):
        rep1 = self.find(num1)
        rep2 = self.find(num2)

        return rep1 == rep2
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        data = UnionSet(n)
        ans = float('inf')
       

        for start,end,leng in roads:
            data.union(start-1,end-1,leng)

        num = data.find(n-1)
        # for i in range(n):
        #     # print("data",data.rep[i],num,data.mini[i],ans)
            
            
        #     if data.rep[i] == num:
                
                
        #         ans = min(ans,data.mini[i])
        

        # print(data.rep,data.mini,data.size)
        return data.mini[data.find(0)]