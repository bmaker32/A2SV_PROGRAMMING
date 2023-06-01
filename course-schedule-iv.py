class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        adj_list = defaultdict(list)
        
        indegrees = [0] * numCourses
        for p,c in prerequisites:
            adj_list[p].append(c)
            indegrees[c] += 1
        
        queue = deque()
        if prerequisites:
            for c in range(numCourses):
                if indegrees[c] == 0:
                    queue.append(c)

        course_prereq = defaultdict(set)
        while queue:
            p = queue.popleft()
            for c in adj_list[p]:
                indegrees[c] -= 1
                course_prereq[c].add(p)
                course_prereq[c].update(course_prereq[p])
                if indegrees[c] == 0:
                    queue.append(c)
        
        return (p in course_prereq[c] for p,c in queries)