class Solution(object):
    def findAnagrams(self, s, p):
        p = list(p)
        p.sort()
        p = "".join(p)
        start = 0
        end = start + len(p) - 1
        s = list(s)
        anagList = s[start: end + 1]
        anagList.sort()
        final = []
        while(end < len(s)):
            anag = "".join(anagList)
            if (anag == p):
                final.append(start)
            anagList.remove(s[start])
            start += 1
            end += 1
            if end >= len(s):
                return final
            bisect.insort(anagList, s[end])
        return final
        