class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(bitvec,slot):
            
            if bitvec == (1<<n)-1:
                return 1
            
            count = 0
            for i in range(1,n+1):
                if (bitvec & 1<<i-1 == 0) and (i%slot==0 or slot%i==0):
                    count += solve(bitvec|1<<i-1,slot+1)
                    
            return count
        
        return solve(0,1)