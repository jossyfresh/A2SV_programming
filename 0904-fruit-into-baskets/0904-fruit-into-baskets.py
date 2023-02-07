class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = Max = 0
        Map = {}
        while r < len(fruits):
            Map[fruits[r]] = r
            if len(Map) > 2:
                x = min(Map.values())
                del Map[fruits[x]]
                l = x+1
            Max = max(Max,r - l+1)
            r+=1

        return Max