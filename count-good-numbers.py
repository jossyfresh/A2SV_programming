class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        def multiply(a, b):
            m = mod
            return ((a % m) * (b % m)) % m

        def binary_exponentiation(base, exponent):
            result = 1
            while exponent > 0:
                if exponent  & 1:
                    result = multiply(base, result)
                base = multiply(base, base)  
                exponent >>= 1
            return result
        even = n//2 + n%2
        odd = n//2
        ans1 = binary_exponentiation(5,even) % mod
        ans2 = binary_exponentiation(4,odd) % mod
        return multiply(ans1,ans2)