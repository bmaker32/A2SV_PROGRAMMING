class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        
        bomb_map = {i: set() for i in range(len(bombs))}
        for i, b1 in enumerate(bombs):
            for j, b2 in enumerate(bombs):
                if i != j:
                    distance = math.sqrt((b1[0] - b2[0])**2 + (b1[1]-b2[1])**2)
                    if distance <= b1[2]:
                        bomb_map[i].add(j)
                    
        def dfs(bomb):
            visited.add(bomb)
            for ngh_bomb in bomb_map[bomb]:
                if ngh_bomb not in visited:
                    dfs(ngh_bomb)
            
        max_bombs_detonated = 0
        for bomb in range(len(bomb_map)):
            visited = set()
            dfs(bomb)
            max_bombs_detonated = max(max_bombs_detonated, len(visited))
        return max_bombs_detonated