class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m-1+n-1)//(factorial(m-1) * factorial(n-1))