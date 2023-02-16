class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        li = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j,matrix[i][j])
                if matrix[i][j] == 0:
                    li.append([i,j])

        for o in range(len(li)):
            k = 0
            while k < len(matrix):
                matrix[k][li[o][1]] = 0
                k += 1
            k = 0
            while k < len(matrix[0]):
                matrix[li[o][0]][k] = 0
                k +=1
                
                    
        