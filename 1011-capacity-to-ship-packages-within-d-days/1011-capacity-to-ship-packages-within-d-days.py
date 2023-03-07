class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        ans = right
        
        def helper(w):
            
            temp = 0
            count = 0
            for i in weights:
                if temp + i <= w:
                    temp += i
                else:
                    temp = 0
                    count += 1
                    temp += i
                    
            return count <days

                
            
     
        while left <= right:
            mid = (left + right)//2
            
            
            
            if helper(mid):
                
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
                
        return ans 
                