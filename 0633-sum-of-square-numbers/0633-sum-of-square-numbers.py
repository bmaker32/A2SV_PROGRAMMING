class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def check(n):
            s = int(math.sqrt(abs(n)))
            return s**2 == n 
        
        for i in range(int(math.sqrt(c))+1):
            a = c - (i**2)
            if check(a):
                return True
        return False
#         else:
#             for i in range(c//2+1):
#                 for k in range(c//2+1):
#                     if i*i + k*k == c:
#                         return True

        
#         return False