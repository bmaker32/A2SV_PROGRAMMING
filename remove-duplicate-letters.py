class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        res = []
        freq =  Counter(s)
        done = {i:False for i in freq.keys()}
        for i in s:
            print(res)
            if done[i]:
                freq[i] -=1
                continue
            while res != [] and res[-1] > i and freq[res[-1]] > 0:
                print(res)
                done[res[-1]] = False
                res = res[:-1]
            res.append(i)
            done[i] = True
            freq[i] -=1     
        return "".join(res)