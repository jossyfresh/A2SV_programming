class Solution:
    def knightDialer(self, n: int) -> int:
        pos = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]

        def isInvalid(r, c):
            if r >= 4 or c >= 3 or r < 0 or c < 0:
                return True
            if (r, c) in [(3, 0), (3, 2)]:
                return True
            return False
        memo = {}
        def countPhoneNumbers(r, c, l):
            if isInvalid(r, c):
                return 0
            if n == l:
                return 1
            if (r, c, l) in memo:
                return memo[(r, c, l)]
            v = 0
            for r0, c0 in pos:
                v += countPhoneNumbers(
                    r + r0, c + c0, l + 1)
            memo[(r, c, l)] = v
            return memo[(r, c, l)] % 1000000007
        mod = 1000000007
        res = 0
        for r in range(4):
            for c in range(3):
                res += countPhoneNumbers(r, c, 1)
        return res % mod