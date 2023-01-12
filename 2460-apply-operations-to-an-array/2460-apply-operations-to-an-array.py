class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        check = True
        count = 0
        n = len(nums)
        i=0
        while i < n:
            
            if nums[i] == 0:
                nums.pop(i)
                count+=1
                n-=1
            else:
                i+=1

        for i in range(count):
            nums.append(0)
        return nums