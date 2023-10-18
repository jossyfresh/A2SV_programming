class Solution:
    def countPrimes(self, n: int) -> int:
        if n > 1:
            check = [True for _ in range(n)]
            check[0] = False
            check[1] = False
            i = 2 
            while i <  n:
                if check[i]:
                    j = i * i
                    while j <  n:
                        check[j] = False
                        j += i
                i+=1
            count = 0
            for x in check:
                if x:
                    count += 1
            return count
        else:
            return 0