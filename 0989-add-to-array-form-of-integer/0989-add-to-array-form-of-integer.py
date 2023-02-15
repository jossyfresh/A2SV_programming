class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num)-1
        val = 0
        for x in num:
            val+=(x*(10**i))
            i-=1
        ans = k+val
        ans = str(ans)
        res = []
        for x in ans:
            res.append(int(x))
        return res