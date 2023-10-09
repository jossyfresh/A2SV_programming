class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l = 0
        r = 0
        ans = []
        while l < len(heaters) and r < len(houses):
            if l < len(heaters)-1:
                if abs(heaters[l] - houses[r]) < abs(heaters[l+1] - houses[r]):
                    ans.append(abs(heaters[l] - houses[r]))
                    r += 1
                else:
                    l += 1
            else:

                ans.append(abs(heaters[l] - houses[r]))
                r += 1
        print(ans)
        return max(ans)