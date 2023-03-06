class Solution:
    def reverse(self,s):
        s = list(s)
        s.reverse()
        return "".join(s)
    def invert(self,s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == "0":
                s[i] = "1"
            else:
                s[i] = "0"
        return "".join(s)
    def sol(self,n,k):
        if n == 0:
            return "0"
        
        s = self.sol(n-1,k)
        s = s + "1" + self.reverse(self.invert(s))
        return s
    
    def findKthBit(self, n: int, k: int) -> str:
        s = self.sol(n,k)
        return s[k-1]
        
    
        
        