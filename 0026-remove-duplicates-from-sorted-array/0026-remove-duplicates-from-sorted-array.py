class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        count = 1
        
        while left < len(nums) and right < len(nums) and  left <= right:
            
            if left == 0:
                left += 1
            elif nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
                count += 1
                right += 1
            else:
                right += 1
        
        return int(count)
         
        
        