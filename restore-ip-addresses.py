class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i, arr):
            if i == len(s) or len(arr) == 4:
                val = ".".join(arr)
                if len(s) ==  len(val)-3:
                    res.append(val)
                return
            for j in range(i + 1, min(i + 4, len(s) + 1)):
                if int(s[i:j]) > 255:
                    return
                arr.append(s[i:j])
                dfs(j, arr)
                arr.pop()
                if s[i] == "0":
                    return
        dfs(0, [])
        return res