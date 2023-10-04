class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        grid = [[float('inf') for i in range(numCourses)] for i in range(numCourses)]
        for x,y in prerequisites:
            grid[x][y] = 1
        for i in range(numCourses):
            grid[i][i] = 0
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
        print(grid)
        ans = [False]*len(queries)
        i = 0
        for x,y in queries:
            if grid[x][y] != float('inf'):
                ans[i] = True
            i += 1
        return ans