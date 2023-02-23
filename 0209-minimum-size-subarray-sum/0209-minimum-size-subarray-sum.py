class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        add = 0
        l = 0
        r = 0
        mini = float(inf)
        sumi = 0
        
        while r < len(nums):
            if sumi < target:
                sumi+=nums[r]
                r+=1
            while sumi >= target:
                if r-l<mini:
                    mini = r-l
                sumi -= nums[l]
                l += 1
        if mini == float(inf):
            return 0
        else:
            return mini
            