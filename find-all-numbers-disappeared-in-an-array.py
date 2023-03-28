class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set()

        for i in range(len(nums)):
            cur = nums[i] - 1
            
            while  cur != i and nums[cur] != nums[i]:
                nums[i], nums[cur] = nums[cur],nums[i]
                ans.discard(cur+1)

                cur = nums[i] - 1
                
                
            if cur != i and  nums[cur] == nums[i]:

                ans.add(i+1)
        
        
        return ans