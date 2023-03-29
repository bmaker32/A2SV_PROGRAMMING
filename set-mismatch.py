class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            cur = nums[i] - 1
            while cur != i and nums[cur] != nums[i]:
                nums[i],nums[cur] = nums[cur],nums[i]
                cur = nums[i] - 1
        print(nums)

        for i in range(len(nums)):

            if (nums[i]-1) != i:
                ans.append( nums[i])
                ans.append(i+1)
        return ans