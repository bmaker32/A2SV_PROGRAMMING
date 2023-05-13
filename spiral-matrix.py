class Solution:
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])
        t = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                t[i][j] = matrix[j][i]
        res = []
        for val in t[::-1]:
            res.append(val)
        return res
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ele = matrix.pop(0)
            #print(ele)
            for i in ele:
                ans.append(i)
            if matrix:
                matrix = self.transpose(matrix)
        return ans