class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        code = False
        
        right= len(arr)-1
        left = 0
        
        while left < len(arr)-1 and arr[left]<arr[left+1]:
            left += 1
            
        while right - 1 > 0 and arr[right] < arr[right-1]:
            right -= 1
            code = True
        print(left,right)
        if left == right and code:
            return True
        return False
        
        
        
                
     
# 
# [1,2,3,4,5,6]
# [1,2,4,3]
# [9,8,7,6,5,4,3,2,1,0]           