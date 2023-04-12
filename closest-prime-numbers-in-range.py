class Solution:
    def closestPrimes(self, left: int, n: int) -> List[int]:
        n += 1
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
        max_ = []
        maxi = (n-1 - left)+10
        prev = -1
        for i in range(left,n):
            if check[i] and prev == -1:
                prev = i
            elif check[i] and prev != -1:
                if i - prev < maxi:
                    max_ = [prev,i]
                    maxi = i - prev
                prev = i
        if not max_:
            return [-1,-1]
        return max_