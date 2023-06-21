class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions) 
        memo = [-1] * n
        def rec_func(index, current_val): 
            if index >= n:
                return current_val
            if memo[index] == -1: 
                points = questions[index][0] 
                brainpower = questions[index][1] 
                a = rec_func(index + brainpower + 1, points) 
                b = rec_func(index + 1, 0) 
                memo[index] = max(a, b) 
            return current_val+memo[index]
        return rec_func(0, 0)