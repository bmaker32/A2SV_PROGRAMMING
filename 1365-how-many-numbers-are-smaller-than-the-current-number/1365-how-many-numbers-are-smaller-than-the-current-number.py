class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums)
        ans=[]
        for i in nums:
            ans.append(nums2.index(i))
        return ans
            
        