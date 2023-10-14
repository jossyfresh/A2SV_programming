# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l = 0
        n = mountain_arr.length()-1
        r = n
        middl = 0
        maps = {}
        while l < r:
            mid = (l + r) // 2
            middle = mountain_arr.get(mid)
            left = mountain_arr.get(mid-1)
            right = mountain_arr.get(mid+1)
            if left < middle < right:
                l = mid + 1
            elif left > middle > right:
                r = mid
            else:
                middl = mid
                break
        def searchIndex(l,r,left):
            if left:
                while l < r:
                    mid = (l+r)//2
                    middle = mountain_arr.get(mid)
                    if middle > target:
                        l = mid+1
                    elif middle < target:
                        r = mid
                    else:
                        return mid
                if mountain_arr.get(r) == target:
                    return r
            else:
                while l < r:
                    mid = (l+r)//2
                    middle = mountain_arr.get(mid)
                    if middle > target:
                        r = mid
                    elif middle < target:
                        l = mid + 1
                    else:
                        return mid
                if mountain_arr.get(r) == target:
                    return r
        left = searchIndex(0,middl,False)
        if left != None:
            return left
        else:
            right = searchIndex(middl,n,True)
            if right:
                return right
        return -1