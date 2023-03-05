class Solution:
    def isPowerOfFour(self, val: int) -> bool:
        if val == 1:
            return True
        elif val < 1:
            return False
        return self.isPowerOfFour(val/4)