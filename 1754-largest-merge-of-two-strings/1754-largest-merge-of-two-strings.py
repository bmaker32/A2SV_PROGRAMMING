class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        d1 = collections.deque(word1)
        d2 = collections.deque(word2)
        merge=[]
        
        while len(d1) > 0 and len(d2) > 0:
            if d1[0] > d2[0]:
                merge.append(d1[0])
                d1.popleft()
            elif d2[0] > d1[0]:
                merge.append(d2[0])
                d2.popleft()
            else:
                if d1 > d2:
                    merge.append(d1[0])
                    d1.popleft()
                else:
                    merge.append(d2[0])
                    d2.popleft()
        merge.extend(d1)
        merge.extend(d2)
        
        return "".join(merge)
        
        