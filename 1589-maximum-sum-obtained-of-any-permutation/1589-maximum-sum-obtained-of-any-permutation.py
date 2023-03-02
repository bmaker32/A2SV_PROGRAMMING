class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        map = [[0,i] for i in range(len(nums))]
        lst = [0]*len(nums)
        add = 0

        for start,end in requests:
            lst[start] += 1
            if end+1 < len(nums):
                lst[end+1] -= 1
            
        lst = list(accumulate(lst))
        nums.sort()
        lst.sort()
        N=1e9 + 7

        for i in range(len(nums)):
           add += nums[i]*lst[i]
        return int(add%N)