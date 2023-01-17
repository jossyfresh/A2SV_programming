class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        up = True
        if n < 3:
            return False
        while i < n-1:
            if i == 0:
                if arr[i] >= arr[i+1]:
                    return False
            else:
                if arr[i] > arr[i+1] and up:
                    up = False
                elif arr[i] == arr[i+1]:
                    return False
                elif arr[i] <= arr[i+1] and not up:
                    return False
            i+=1 
        if up:
            return False
        else:
            return True
                
            