class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dictt = {0:1}
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        counter = 0
        s = 0
        
        for i in nums:
            s += i
            
            if s-k in dictt:
                counter += dictt[s-k]
            if s in dictt:
                dictt[s] += 1
            else:
                dictt[s] = 1
                
            
        return counter 
        
        
                
            
            
                
                