class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = format(x,'032b')
        by = format(y,'032b')
        count = 0
        for i in range(32):
            if bx[i] != by[i]:
                count += 1
        return  count