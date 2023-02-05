class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mapp = {}
        maps = {}
        res = []
        l = 0
        if len(s)>=len(p):
            for i in range(len(p)):
                mapp[p[i]] = 1 + mapp.get(p[i],0)
                maps[s[i]] = 1 + maps.get(s[i],0)
        else:
            return []
        if mapp == maps:
            res.append(l)
        for r in range(len(p),len(s)):
            maps[s[r]] = 1 + maps.get(s[r],0)
            if maps.get(s[l],0) == 1:
                maps.pop(s[l])
            else:
                maps[s[l]] = maps.get(s[l],0) - 1
            l+=1
            if mapp == maps:
                res.append(l)
        return res