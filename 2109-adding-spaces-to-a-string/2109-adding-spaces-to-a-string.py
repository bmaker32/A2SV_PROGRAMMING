class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        le = list(s)
        ans = []
        
        for i in range(len(spaces)):
            if i != 0:
                ans.append(s[spaces[i-1]:spaces[i]])
            else:
                ans.append(s[:spaces[i]])
        ans.append(s[spaces[-1]:])
        print(ans)
        return " ".join(ans)
            
            