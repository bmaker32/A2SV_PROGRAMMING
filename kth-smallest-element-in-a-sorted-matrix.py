class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0], (0,0))]
        dirs = [(1,0), (0,1), (1,1)]
        visited = set()
       
        while heap:
            cur, (i,j) = heapq.heappop(heap)
            count += 1
           
            if count == k:
                return cur

            for dir_ in dirs:
                ix, jx = dir_
                i_new, j_new = i+ix, j+jx
               
                if i_new < m and j_new < n:
                    if (i_new, j_new) not in visited:
                        visited.add((i_new, j_new))
                        heapq.heappush(heap, (matrix[i_new][j_new], (i_new, j_new)))