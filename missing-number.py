class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = 0

        for i in range(len(nums)):
            cur = nums[i]

            while nums[i] < len(nums) and cur != i:
                nums[i], nums[cur] = nums[cur],nums[i]
                cur = nums[i] 

        print(nums)
                
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)