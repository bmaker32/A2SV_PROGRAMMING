class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        arr = [1]*(rowIndex + 1)
        top = self.getRow(rowIndex-1)
        
        for i in range(1,rowIndex):
            arr[i] = top[i-1] + top[i]
        return arr