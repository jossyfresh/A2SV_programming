class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(sqrt(c))
        l = 0
        while l <= r:
            if (l*l) + (r*r) > c:
                r-=1
            elif (l*l) + (r*r) < c:
                l+=1
            else:
                return True
        return False
        
        