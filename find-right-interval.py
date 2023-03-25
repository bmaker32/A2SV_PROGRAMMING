class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n
        for i in range(len(intervals)):
            intervals[i].append(i)

        intervals.sort()
        temp = [i[0] for i in intervals]

        for l, r, i in intervals:
            x = bisect_left(temp, r)
            if(x != n):
                ans[i] = intervals[x][2]
        return ans