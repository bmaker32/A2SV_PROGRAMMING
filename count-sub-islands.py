class Solution:
    def countSubIslands(self, G1: List[List[int]], G2: List[List[int]]) -> int:
        N, M = len(G1), len(G1[0])
        def dfs(r, c):
            if not(0<=r<N and 0<=c<M) or G2[r][c]==0:
                return True
            G2[r][c] = 0
            ok = G1[r][c] == 1
            if not dfs(r-1, c): ok = False
            if not dfs(r+1, c): ok = False
            if not dfs(r, c+1): ok = False
            if not dfs(r, c-1): ok = False
            return ok
        return sum(G2[i][j] and dfs(i, j) for j in range(M) for i in range(N))