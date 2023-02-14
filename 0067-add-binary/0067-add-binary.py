class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rem = 0
        l = len(a)-1
        r = len(b)-1
        ans = []
        while l >= 0 and r>=0:
            if a[l] =="1"and b[r]=="1":
                if rem == 0:
                    ans.append("0")
                else:
                    ans.append("1")
                rem=1
            elif a[l]=="1" or b[r]=="1":
                if rem:
                    ans.append("0")
                    rem = 1
                else:
                    ans.append("1")
                    rem = 0
            else:
                if rem:
                    ans.append("1")
                else:
                    ans.append("0")
                rem = 0
            r-=1
            l-=1
        while l>=0:
            if a[l] == "1":
                if rem:
                    ans.append("0")
                    rem = 1
                else:
                    ans.append("1")
                    rem = 0
            else:
                if rem:
                    ans.append("1")
                else:
                    ans.append("0")
                rem = 0
            l-=1
        while r >= 0:
            if b[r] == "1":
                if rem:
                    ans.append("0")
                    rem = 1
                else:
                    ans.append("1")
                    rem = 0
            else:
                if rem:
                    ans.append("1")
                else:
                    ans.append("0")
                rem = 0
            r-=1
        if rem:
            ans.append("1")
        res = ""
        for i in range(len(ans)-1,-1,-1):
            res+=ans[i]
        return res         
            