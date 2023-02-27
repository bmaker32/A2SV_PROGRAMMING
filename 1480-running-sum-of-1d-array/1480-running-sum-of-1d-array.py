class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acum = list(accumulate(nums))
        return acum