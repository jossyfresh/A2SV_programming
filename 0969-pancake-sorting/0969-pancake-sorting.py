class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k =[]
        x = arr.copy()
        x.sort()
        for i in range(len(arr)):
            if arr == x:
                break
            maxi = max(arr[:n-i])
            max_ = arr.index(maxi) + 1
            arr[:max_] = reversed(arr[:max_])
            k.append(max_)
            k.append(n-i)
            arr[:n-i] = reversed(arr[:n-i])
        return k
