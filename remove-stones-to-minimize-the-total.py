class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for pile in piles:
            heapq.heappush(max_heap, -pile)

        for _ in range(k):
            pile = heapq.heappop(max_heap)
            pile = math.ceil(-pile/2)
            heapq.heappush(max_heap, -pile)
        
        return -sum(max_heap)