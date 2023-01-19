class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        le = len(matrix)
        check = True
        for i in range(le-1):
            for j in range(len(matrix[i])-1):
                
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
                    
                
                
                
                    
                    
                    
        
        