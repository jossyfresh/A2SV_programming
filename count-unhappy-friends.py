class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = {}
        p = {}
        for idx,e in enumerate(preferences):
            d[idx] = e
        c = set()
        for x,y in pairs:
            p[x] = y
            p[y] = x
        for i in range(n):
            team = p[i]
            temp = []
            for m in d[i]:
                if m == team:
                    break
                temp.append(m)
            for k in temp:
                if d[k].index(i) < d[k].index(p[k]):
                    c.add(i)

        return len(c)