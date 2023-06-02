class Solution(object):
    def isBipartite(self, i, graph, color):
        color[i] = 1
        queue = deque([(i)])
        
        while queue:
            vertex = queue.popleft()
            for neighbour in graph[vertex]:
                if color[neighbour] == color[vertex]:
                    return False
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[vertex]
                    queue.append((neighbour))
        return True
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        color = [-1]*(n+1)
        graph = {i:[] for i in range(1, n + 1)}
        
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        
        
        for i in range(1, n + 1):
            if color[i] == -1:
                if not self.isBipartite(i, graph, color):
                    return False
        return True