class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        visited = set()
        queue.append(0)
        while queue:
            n = len(queue)
            while n:
                n-=1
                room = queue.popleft()
                visited.add(room)
                if len(visited) == len(rooms):
                    return True
                for keys in rooms[room]:
                    if keys not in visited:
                        queue.append(keys)
                        visited.add(keys)
        return False