class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[0:k]) / k
        tot = sum(nums[0:k])
        l = 0
        r = k
        while r < len(nums):
            tot -= nums[l]
            tot += nums[r]

            avg = tot / k
            ans = max(ans,avg)
            r += 1
            l += 1
        return ans