class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans =[]
        
        
        for i in range(len(grid)):
            temp =[]
            for j in range(len(grid[0])):
                maxi = -1
                if (len(grid[0])-j)>=3:
                    if i + 3 <= len(grid):
                        for k in range(i,i+3):
                            maxi = max(maxi,max(grid[k][j:j+3]))
                        temp.append(maxi)
            if temp != []:
                ans.append(temp)
        return ans
                        
                    