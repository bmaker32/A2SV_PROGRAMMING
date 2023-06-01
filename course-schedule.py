class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        indegrees = [0]*numCourses
        for p in prerequisites:
            graph[p[0]].append(p[1])
            indegrees[p[1]] += 1
        
        q = deque()
        processed = 0
        for i, x in enumerate(indegrees):
            if not x:
                q.append(i)
            
        while q:
            course = q.popleft()
            processed += 1
            for c in graph[course]:
                indegrees[c] -= 1
                if not indegrees[c]:
                    q.append(c)
            
        return processed == numCourses