class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()

        for i in range(len(nums)):
            cur = nums[i] - 1
            while cur != i and nums[cur] != nums[i]:
                nums[i],nums[cur] = nums[cur],nums[i]
                cur = nums[i] - 1
            
            if cur != i and nums[cur] == nums[i]:
                ans.add(nums[i])
        
        return ans