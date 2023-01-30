class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        k = len(nums)
        count = 1
            
        for i in range(k):
            n = nums[i]
            sign = n //abs(n) 
            n = abs(n) 
            cnt = int(str(n)[::-1])*sign
            nums.append(cnt)
        return len(set(nums))
        
        
            
        