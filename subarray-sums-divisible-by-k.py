class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        maps = defaultdict(int)
        maps[0] += 1
        prefix = []
        counter = 0
        
        prefix.extend(accumulate(nums))
        
        
        for i in prefix:
            
            if i%k in maps:
                counter += maps[i%k]
            maps[i%k] += 1
            
        return counter