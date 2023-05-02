class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(maze) and 0 <= col < len(maze[0]))
        def out(row,col):
            if 0 == row or row == len(maze)-1 or 0 == col or col == len(maze[0])-1:
                if maze[row][col] == "." and [row,col] != entrance :
                    return True
            return False
        queue.append(tuple(entrance))
        len_ = 0
        visited = set()
        while queue:
            n = len(queue)
            while n:
                n -=  1
                i,j = queue.popleft()
                if out(i,j):
                    print(i,j)
                    return len_
                for x,y in direction:
                    if inbound(x+i,y+j) and (x+i,y+j) not in visited and maze[x+i][y+j] == ".":
                        queue.append((x+i,y+j))
                        visited.add((x+i,y+j))
            len_+=1
        return -1