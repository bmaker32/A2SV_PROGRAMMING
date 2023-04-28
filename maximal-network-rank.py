class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        g = defaultdict(list)
        
        for u, v in roads:  
            g[u].append(v)
            g[v].append(u)
        
        res = 0
        
        for i in range(n):
            for j in range(i+1, n):
                val = len(g[i]) + len(g[j]) 
                if j in g[i]:  
                    val -= 1
                res = max(res, val)
        
        
        return res