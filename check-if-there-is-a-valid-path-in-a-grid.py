class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rep = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rep[(i,j)] = (i,j)
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        destination = {1:(0,-1,0,1),2:(1,0,-1,0),3:(0,-1,1,0),4:(0,1,1,0),5:(0,-1,-1,0),6:(0,1,-1,0)}
        novalid = [(1,2),(1,4),(1,6),(2,1),(2,3),(2,4),(3,1),(3,4),(6,3),(5,6),(3,3),(4,4),(5,5),(6,6)]
        novalid = set(novalid)
        def find(x):
            number = x
            while number != rep[number]:
                number = rep[number]
            return number
        def union(x,y):
            repx = find(x)
            repy = find(y)
            if repx != repy:
                rep[repy] = repx
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x = (i,j)
                move = destination[grid[i][j]]
                newi = i + move[0]
                newj = j + move[1]
                newx = i + move[2]
                newy = j + move[3]
                mn = grid[i][j]
                if inbound(newi,newj):
                    xn = grid[newi][newj]
                    if (xn,mn) not in novalid:
                        union((newi,newj),x)
                if inbound(newx,newy):
                    yn = grid[newx][newy]
                    if (mn,yn) not in novalid:
                        union(x,(newx,newy))
        end = find((len(grid)-1,len(grid[0])-1))
        start = find((0,0))
        print(end)
        print(start)
        return start == end