class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(maps,mapt):
            for key in mapt:
                if key not in maps or mapt[key] > maps[key]:
                    return False
            return True
        if len(s) < len(t):
            return ""
        nt = Counter(t)
        ns = {}
        res = []
        r = 0
        l = 0
        while r < len(s):
            if s[r] in nt:
                ns[s[r]] = ns.get(s[r],0)+1
            if valid(ns,nt):
                while valid(ns,nt):
                    if s[l] in ns:
                        ns[s[l]] -= 1
                        if ns[s[l]] == 0:
                            ns.pop(s[l])
                    l+=1
                res.append([r,l])
            r+=1
        max_ = len(s)
        if len(res) == 0:
            return ""
        for x in res:
            if x[0] - x[1] < max_:
                r = x[0]
                l = x[1]-1
                max_ = x[0] - (x[1])
        print(l)
        print(r)
        return s[l:r+1]