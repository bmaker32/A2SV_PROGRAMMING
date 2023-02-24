class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        maps = defaultdict(int)
        prefix = [0]
        count = 0
        
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        
        for s in prefix:
            if (s-k) in maps:
                count += maps[s-k]            
            maps[s]+=1
            
        return count 