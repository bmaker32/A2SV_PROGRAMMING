class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        
        piles.sort()
        j=len(piles)-1
                
        for i in range(len(piles)):
            pi=[]
            if i <= j:
                pi.append(piles[j])
                pi.append(piles[j-1])
                pi.append(piles[i])
                ans += pi[1]
                j-=2
            else:
                break
        return ans
            