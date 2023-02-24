class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        
        for i,val in enumerate(nums):
            
            if val in maps :
                return [maps[val],i]
            maps[target-val] = i
            