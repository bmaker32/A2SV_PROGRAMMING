class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        mapping = {}
        for r, k in enumerate(rooms):
            mapping[r] = k
        seen = set()
        q = collections.deque()
        q.append(0)
        while q:
            room = q.popleft()
            seen.add(room)
            for key in mapping[room]:
                if key not in seen:
                    if key == room:
                        return False
                    q.append(key)
        return len(seen) == len(mapping)