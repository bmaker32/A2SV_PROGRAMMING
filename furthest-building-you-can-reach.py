class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        N = len(heights)
        heap = []

        for i in range(N-1):
            h = heights[i+1] - heights[i]
            if h <= 0: continue
            heappush(heap,h)
            if len(heap) > ladders:
                minx = heappop(heap)
                bricks -= minx
            if bricks < 0: return i
        return N-1