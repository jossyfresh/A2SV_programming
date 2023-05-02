class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))
        queue =  deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]== 0:
                    queue.append((i,j))
                    visited.add((i,j))
        ans = mat[:]
        while queue:
            n = len(queue)
            while n:
                n -= 1
                i,j = queue.popleft()
                for x,y in direction:
                    if inbound(x+i,y+j) and (x+i,y+j) not in visited:
                        queue.append((x+i,y+j))
                        visited.add((x+i,y+j))
                        ans[x+i][y+j] = ans[i][j] + 1
        return ans