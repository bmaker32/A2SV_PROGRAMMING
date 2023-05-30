class Unions:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        self.components = N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ua = self.find(a)
        ub = self.find(b)
        if ua == ub:
            return False

        if self.size[ua] < self.size[ub]:
            ua, ub = ub, ua

        self.parent[ub] = ua
        self.size[ua] += self.size[ub]
        self.size[ub] = self.size[ua]
        self.components -= 1
        return True

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        uf = Unions(N)
        
        mapPointsToIdx = defaultdict(int)
        i = 0
        for x, y in points:
            mapPointsToIdx[(x, y)] = i
            i += 1
        
        minH = []
        for i in range(N):
            for j in range(i + 1, N):
                xa, ya = points[i]
                xb, yb = points[j]
                distance = abs(xa - xb) + abs(ya - yb)
                heappush(minH, (distance, (xa, ya), (xb, yb)))

        ans = 0
        while uf.components > 1 and minH:
            d, a, b = heappop(minH)
            aIdx = mapPointsToIdx[a]
            bIdx = mapPointsToIdx[b]
            if uf.union(aIdx, bIdx):            
                ans += d
        return ans