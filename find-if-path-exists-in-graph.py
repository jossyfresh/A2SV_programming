class Solution:
    def validPath(self, n: int, con: List[List[int]], source: int, des: int) -> bool:
        adjlist = {i:[] for i in range(n)}
        for x,y in con:
            adjlist[x].append(y)
            adjlist[y].append(x)
        visited = set()
        visited.add(source)
        stack = [source]
        if source == des:
            return True
        while stack:
            for x in adjlist[stack.pop()]:
                if x not in visited:
                    visited.add(x)
                    if x == des:
                        return True
                    stack.append(x)
        return False