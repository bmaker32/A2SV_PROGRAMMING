class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums.extend(int(str(n)[::-1]) for n in reversed(nums))
        return len(set(nums))
        
        
            
        