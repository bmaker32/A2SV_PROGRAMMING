class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen = set()

        def dfs(idx,sequence):
            
            
            if idx == len(nums):
                if len(sequence) >= 2:
                    seen.add(tuple(sequence))
                return

            if not sequence or nums[idx] >= sequence[-1] :
                dfs(idx+1,sequence+[nums[idx]])

            dfs(idx+1,sequence)

        dfs(0,[])
        return seen