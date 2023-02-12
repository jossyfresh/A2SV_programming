class Solution:
    def isHappy(self, n: int) -> bool:
        def nextnum(n):
            nex = 0
            for x in n:
                nex+=int(x)**2
            return str(nex)
        n = str(n)
        vals = set()
        while nextnum(n) not in vals:
            nex = nextnum(n)
            print(nex)
            if nex == "1":
                return True
            vals.add(nex)
            n = str(nex)
        return False