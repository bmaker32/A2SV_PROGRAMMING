class Solution: 
    def dfs(self, graph: List[List[int]], root: int)-> List[List[int]]:
        ans = []
        n = len(graph)
        if (root == self.nodes - 1):
            return [[root]]
        m = len(graph[root])

        for i in range(0, m):
            neighbor = graph[root][i]
            subpaths = self.dfs(graph, neighbor)
            for path in subpaths:
                ans.append([root] + path)
        return ans

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.nodes = len(graph)
        return self.dfs(graph, 0)