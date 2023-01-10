class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums2 = list(nums)
        for i in range(len(nums)):
            nums2[i] = nums[nums[i]]
        return nums2