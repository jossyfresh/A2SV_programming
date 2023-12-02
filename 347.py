class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        maparr = {}
        res = []
        for x in arr:
            maparr[x] = maparr.get(x,0)+1
        ordered = sorted(maparr.items(), key=lambda x: x[1],reverse = True)
        
        for i in range(0,k):
            res.append(ordered[i][0])
        
        return res

        
