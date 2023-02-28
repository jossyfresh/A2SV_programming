class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 
        val = self.myPow(x,int(n/2))
        if n%2 == 0:
            return val*val
        elif n%2 != 0:
            if n > 0:
                return x*val*val
            else:
                return (val*val)/x