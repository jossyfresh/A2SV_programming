class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(arr):
            if len(arr)  > 1 and arr[0] == "0":
                return True
        def dfs(val,val1,indx):
            if indx == len(num):
                return True
            for l in range(indx,len(num)):
                n = num[indx:l+1]
                if check(n):
                    break
                n = int(n)
                if  val + val1 == n and dfs(val1,n,l+1):
                    return True
            return False

        for i in range(len(num)-2):
            val = num[:i+1]
            if check(val):
                break
            val = int(val)
            for j in range(i+1,len(num)-1):
                val1 = num[i+1:j+1]
                if check(val1):
                    break
                val1 = int(val1)
                print(f'{val} {val1} {j+1}')
                if dfs(val,val1,j+1):
                    return True
        return False