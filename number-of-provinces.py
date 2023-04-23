class Solution:  
    def __init__(self):
        self.seen = set()
        
    def dfs(self, isConnected, i):
        self.seen.add(i)
        
        for j in range(len(isConnected[i])): 
            if isConnected[i][j] == 1 and j not in self.seen:
                self.dfs(isConnected, j)
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(isConnected)):
            if i not in self.seen:
                self.dfs(isConnected, i)
                res += 1
            
        return res