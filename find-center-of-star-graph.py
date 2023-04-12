class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        for x,y in edges:
            adjlist[y].append(x)
            adjlist[x].append(y)
        len_ = len(adjlist)
        for x in adjlist:
            if len(adjlist[x]) == len_ - 1:
                return x