class Solution:
    def convert(self, s: str, row: int) -> str:
        down = True
        i = 0
        ans = [[] for i in range(row)]
        if row == 1:
            return s
        for l in s:
            ans[i].append(l)
            if i == row-1 and down:
                down = False
                i-=1
            elif i == 0 and not down:
                down =True
                i+=1
            elif down:
                i+=1
            elif not down:
                i-=1
        return ("".join(list("".join(i) for i in ans)))  
        