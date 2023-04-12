class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        a = set()
        def prime(n):
            d = 2
            i = n
            while d * d <= n:
                while i % d == 0:
                    a.add(d)
                    i //= d
                d+=1
            if i > 1:
                a.add(i)
        for x in nums:
            prime(x)
        return len(a)