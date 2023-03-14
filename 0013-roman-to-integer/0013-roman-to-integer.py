class Solution(object):
    def romanToInt(self, s):
        key={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prevC=s[0]
        sum=0
        for c in s:
            if key[prevC]<key[c]:
                sum-=key[prevC]*2
            sum+=key[c]
            prevC=c
        return sum