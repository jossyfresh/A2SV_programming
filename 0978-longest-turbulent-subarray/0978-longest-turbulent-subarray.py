class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        r = 1
        l = 0
        max_ = 0
        prev = arr[0]
        if len(arr) == 1:
            return 1
        up = True
        while r < len(arr):
            if prev > arr[r]:
                up = True
                break
            elif prev < arr[r]:
                up = False
                break
            prev = arr[r]
            r+=1
            
        l = r-1   
        while r < len(arr):
            cur = arr[r]
            if up and prev > cur:
                prev = cur
                r+=1
                up = False
            elif not up and prev < cur:
                prev = cur
                r+=1
                up = True
            else:
                max_ = max(max_,r-l)
                while r < len(arr):
                    if prev > arr[r]:
                        up = True
                        break
                    elif prev < arr[r]:
                        up = False
                        break
                    prev = arr[r]
                    r+=1
                l = r-1
        max_=max(max_,(r-l))
        return max_
        