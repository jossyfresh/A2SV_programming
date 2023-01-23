class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            start = 1
            prev = 0
            for i in range(n):
                start+=prev
                prev = start-prev
            return start
                
            