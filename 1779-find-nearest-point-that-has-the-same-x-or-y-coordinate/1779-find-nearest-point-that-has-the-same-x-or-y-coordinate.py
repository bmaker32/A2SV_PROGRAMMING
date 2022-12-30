class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mini=-1
        minind=-1
        for i in points:
            if i[0] == x or y == i[1]:
                print("here")
                if mini == -1:
                    print("assign mini from -1")
                    minind = points.index(i)
                    mini = abs(x-i[0])+abs(y-i[1])
                elif mini > abs(x-i[0])+abs(y-i[1]):
                    print("another")
                    minind = points.index(i)
                    mini = abs(x-i[0])+abs(y-i[1])
        return minind