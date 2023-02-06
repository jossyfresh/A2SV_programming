class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n =  len(nums1)
        m = len(nums2)
        mid = []
        l = 0
        r = 0
        k = ((n+m)//2)+1
        while r < m and l < n:
            if k > 0:
                if nums1[l] < nums2[r]:
                    mid.append(nums1[l])
                    l+=1
                else:
                    mid.append(nums2[r])
                    r+=1
                k-=1
            else:
                break
        if k > 0:
            while l < n:
                if k > 0:
                    mid.append(nums1[l])
                    l+=1
                    k-=1
                else:
                    break
            while r < m:
                if k > 0:
                    mid.append(nums2[r])
                    r+=1
                    k-=1
                else:
                    break
        if (n+m)%2 == 0:
            return float((mid[-1]+mid[-2])/2)
        else:
            return float(mid[-1])
        
    
            
            