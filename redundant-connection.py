class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i:i for i in range(1,len(edges)+1)}
        def find(x):
            number = x
            while number != rep[number]:
                number = rep[number]
            return number
        ans = []
        flag = 0
        def union(x,y):
            nonlocal flag
            repx = find(x)
            repy = find(y)
            if repx == repy:
                ans.append(x)
                ans.append(y)
            else:
                rep[repy] = repx
        for x,y in edges:
            union(x,y)
        return ans