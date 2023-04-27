class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0),(-1,-1),(-1,1),(1,-1),(1,1)]
        queue = deque()
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        if grid[0][0] == 0:
            queue.append((0,0))
            visited = set()
            len_ = 0
            while queue:
                n = len(queue)
                while n:
                    i,j = queue.popleft()
                    visited.add((i,j))
                    n -= 1
                    if (i,j) == (len(grid)-1,len(grid[0])-1):
                        return len_ + 1
                    for x,y in direction:
                        if inbound(x+i,y+j) and (x+i,y+j) not in visited and grid[x+i][y+j] == 0:
                            queue.append((x+i,y+j))
                            visited.add((x+i,y+j))
                len_ += 1 
        return -1