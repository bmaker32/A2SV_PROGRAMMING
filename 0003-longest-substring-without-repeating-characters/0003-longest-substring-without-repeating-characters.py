class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxi = 0
        sets = set()
        
        
        
        while r < len(s):
            if s[r] in sets:
                
                while s[r] in sets:
                    sets.remove(s[l])
                    l+=1
            maxi = max(maxi,r-l+1)
            sets.add(s[r])
            r += 1
            
            
        return maxi