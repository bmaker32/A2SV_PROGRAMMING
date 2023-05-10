class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m ,n = len(maze),len(maze[0])
        # visited = set()
        q = deque()
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        
        q.append((0,(entrance[0],entrance[1])))
        # print(q)
        maze[entrance[0]][entrance[1]] = '+'
        
        
        while q:
            # print("loop")
            steps,temp = q.popleft()
            r,c = temp[0],temp[1]

            if steps != 0 and ((r) == (m-1) or c == (n-1) or r == 0 or c == 0):
                return steps 

            for i,j in dirs:
                # print("hello")
                new_r = r + i
                new_c = c + j

                if 0<= new_r < m and 0<= new_c < n and maze[new_r][new_c]=='.':
                    # print(new_r,new_c)
                    q.append((steps+1,(new_r,new_c)))
                    maze[new_r][new_c] = '+'
        return -1