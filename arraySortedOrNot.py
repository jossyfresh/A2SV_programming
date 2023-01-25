
class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        l = 0
        r =1
        while r < len(arr):
            if arr[l] > arr[r]:
                return False
            l+=1
            r+=1
        return True
