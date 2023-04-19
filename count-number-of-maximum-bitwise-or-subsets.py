class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxPossible = 0
        
        for n in nums:
            maxPossible |= n
        
        ans = [0]
        
        def solve(nums, index, prev, maxPossible):
            if index == len(nums):
                return
            
            curr = prev | nums[index]
            
            if curr == maxPossible:
                ans[0] += 1
            
            solve(nums, index + 1, curr, maxPossible)
            solve(nums, index + 1, prev, maxPossible)
        
        solve(nums, 0, 0, maxPossible)
        return ans[0]