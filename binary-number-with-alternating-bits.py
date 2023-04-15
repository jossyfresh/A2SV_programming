class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        while n:
            if prev == -1:
                prev = n&1
            else:
                if prev == n&1:
                    return False
                else:
                    prev = n&1
            n >>= 1
        return True