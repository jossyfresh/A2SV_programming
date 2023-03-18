class Solution:
    def balancedString(self, s: str) -> int:
        def check(let,lit):
            for x in let:
                if x not in lit or lit[x] < let[x]:
                    return False
            return True
        maps = Counter(s)
        let = {}
        lit = {}
        for x in maps:
            if maps[x] > len(s)/4:
                let[x] = maps[x]-len(s)//4
        if len(let) == 0:
            return 0
        i = 0 
        dq = deque()
        max_ = len(s)
        while i < len(s):
            while dq and check(let,lit):
                max_ = min(max_,len(dq))
                y = dq.popleft()
                if y in lit:
                    lit[y] -= 1
                    if lit[y] == 0:
                        lit.pop(y)
            dq.append(s[i])
            if s[i] in let:
                lit[s[i]] = lit.get(s[i],0) + 1
            i+=1
        while dq and check(let,lit):
            max_ = min(max_,len(dq))
            y = dq.popleft()
            if y in lit:
                lit[y] -= 1
                if lit[y] == 0:
                    lit.pop(y)
        return max_