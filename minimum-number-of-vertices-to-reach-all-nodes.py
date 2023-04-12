class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjlist = {i:[] for i in range(n)}
        for x,y in edges:
            adjlist[y].append(x)
        ans = []
        for x in adjlist:
            if not adjlist[x]:
                ans.append(x)
        return ans