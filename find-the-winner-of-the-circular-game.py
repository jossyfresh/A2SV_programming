class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num = [True for i in range(n)]
        count = n
        i = 0
        while True:
            if count == 1:
                break
            j = k
            while j > 1:
                if num[i] == True:
                    j -= 1
                if i == len(num)-1:
                    i = 0
                else:
                    i += 1
            while num[i] == False:
                if i == len(num)-1:
                    i = 0
                else:
                    i += 1
            num[i] = False
            count -= 1
        for i in range(len(num)):
            if num[i]:
                return i+1