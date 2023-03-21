class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        cummG = [0]*(n+1)
        for i in range(n-1,-1,-1):
            cummG[i] = cummG[i+1] + grid[0][i]
        lsum = 0
        ans = math.inf
        for i in range(n):
            ans = min(ans,max(cummG[i+1],lsum))
            lsum+=grid[1][i]
        return ans