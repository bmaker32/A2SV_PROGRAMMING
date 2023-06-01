class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        nums.sort()
        left3, right3 = nums[-1]-nums[3], nums[-4]-nums[0]
        l1r2, l2r1 = nums[-3]-nums[1], nums[-2]-nums[2]
        return min(left3, right3, l1r2, l2r1)