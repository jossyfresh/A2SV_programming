class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        rep = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]
        def union(x,y):
            repx = find(x)
            repy = find(y)
            if repx == repy:
                return 
            if rank[repx] < rank[repy]:
                repx,repy = repy,repx
            rep[repy] = repx
            rank[repx] += rank[repy]
            return repx
        meetings.sort(key=lambda x:x[2])
        meet = defaultdict(list)
        for i in range(len(meetings)):
            x,y,z = meetings[i]
            meet[z].append((x,y))                                               
        union(0,firstPerson)
        head = 0
        for z in meet:
            visit = set()
            for x,y in meet[z]:
                repxy = union(x,y)
                if repxy is None:
                    continue
                head = rep[head]
                if repxy != head:
                    visit.add(x)
                    visit.add(y)
            for x in visit:
                if find(x) != head:
                    rep[x] = x
                    rank[x] = 1
        ans = []
        for i in range(n):
            if find(i) == head:
                ans.append(i)
        return ans



