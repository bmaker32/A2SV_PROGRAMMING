class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        valid = {(i, j) for i in range(len(grid)) for j in range(len(grid[0]))}
        
        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + sum([
                dfs(i+1, j) if (i+1, j) in valid else 0,
                dfs(i, j+1) if (i, j+1) in valid else 0,
                dfs(i-1, j) if (i-1, j) in valid else 0,
                dfs(i, j-1) if (i, j-1) in valid else 0
            ])
        
        return max([dfs(i, j)  if grid[i][j] else 0 for i in range(len(grid)) for j in range(len(grid[0]))])