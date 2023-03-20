class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def calc(arr):
            for i in range(len(arr)):
                arr[i] = sorted(arr[i])
            mw = {}
            for i,x in enumerate(arr):
                s = Counter(x)
                l = x[0]
                mw[i] = s[l]
            return mw
        ans = [0]*len(queries)
        mq = calc(queries)
        mw = calc(words)
        for x in mq:
            key = x
            for y in mw:
                if mq[key] < mw[y]:
                    ans[key] += 1
        return ans