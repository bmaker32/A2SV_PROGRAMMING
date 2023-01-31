class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = list(nums)
        # j = k-1
        for i in range(len(nums)):
            
            # if i + k < len(nums):
            nums[(i + k) % len(n)] = n[i]
        nums = list(n)
        
        