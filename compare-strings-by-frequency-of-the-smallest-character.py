class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            if not s: return 0
            count = 1
            smallest = s[0]
            for i in s[1:]:
                if i < smallest:
                    smallest = i
                    count = 1
                elif i == smallest:
                    count += 1
            return count
        
        res = []
        countw = Counter([f(i) for i in words])
        
        for i in queries:
            temp1 = f(i)
            temp2 = 0
            for key in countw:
                if key > temp1:
                    temp2 += countw[key]
            res.append(temp2)
        return res