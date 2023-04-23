class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        colr = image[sr][sc]
        def dfs(i,j):
            visited.add((i,j))
            image[i][j] = color
            for x,y in directions:
                newi = x + i
                newj = y + j
                if inbound(newi,newj) and (newi,newj) not in visited and image[newi][newj] == colr:
                    dfs(newi,newj)
        dfs(sr,sc)
        return image