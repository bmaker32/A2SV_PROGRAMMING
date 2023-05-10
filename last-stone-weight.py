class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            # print("in")
            s1 = stones.pop()
            s2 = stones.pop()
            s1 = abs(s1-s2)
            if s1 > 0:
                stones.append(s1)
            # print(stones)
        if len(stones) == 0:
            return 0
        # print(stones[0])
        return stones[0]