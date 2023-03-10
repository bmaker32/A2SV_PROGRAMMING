class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        map = defaultdict(int)
        map[0] = 1
        prefix = list(accumulate(nums))
        counter = 0
        print(prefix)

        for i in prefix:
            if i - goal in map:
                counter += map[i-goal] 
            map[i] += 1
        


        return counter