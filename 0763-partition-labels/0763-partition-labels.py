class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maps = {}
        size = 0
        res = []
        for i,x in enumerate(s):
            maps[x] = i 
        y = maps.get(s[0],0)
        for i in range(len(s)):
            if maps.get(s[i],0) >= y:
                y = maps.get(s[i],0)
            if i == y:
                res.append(size+1)
                size = 0
            else:
                size+=1
        return res