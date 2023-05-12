class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def isMagic(sub_grid):
            arr = []
            for i in range(len(sub_grid)):
                for j in range(len(sub_grid[0])):
                    arr.append(sub_grid[i][j])
            if sorted(arr) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False

            if sum(sub_grid[0]) != sum(sub_grid[1]) != sum(sub_grid[2]):
                return False
            r_sum = sum(sub_grid[0])

            if r_sum != (sub_grid[0][0] + sub_grid[1][0] + sub_grid[2][0]) != (sub_grid[0][1] + sub_grid[1][1] + sub_grid[2][1]) != (sub_grid[0][2] + sub_grid[1][2] + sub_grid[2][2]):
                return False
            
            if r_sum != (sub_grid[0][0] + sub_grid[1][1] + sub_grid[2][2]):
                return False
            
            return True

        res = 0
        for i in range(m-2):
            for j in range(n-2):
                sub_grid = [[grid[x][y] for y in range(j, j+3)] for x in range(i, i+3)]
                if(isMagic(sub_grid)):
                    res += 1
        return res