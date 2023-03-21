class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        M = 10**9+7
        sumMin = 0
        arr.append(0)  
        stack = [-1]  
        
        
        for cur_idx, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                idx = stack.pop()
                pre_min = stack[-1]
                sumMin += (idx - pre_min) * (cur_idx - idx) * arr[idx]
            stack.append(cur_idx)
        
        return sumMin%M