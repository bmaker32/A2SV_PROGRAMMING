class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ma = -1
        
        for i in range (len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = ma
            ma = max(ma,temp)
                
                
        return arr
                
        