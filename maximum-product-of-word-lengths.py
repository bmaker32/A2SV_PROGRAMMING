class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        words = list(set(words))
        for i in words:
            for j in words:
                if all(a not in b for a in i for b in j):
                    ans = max(ans , len(i)* len(j))
        return ans