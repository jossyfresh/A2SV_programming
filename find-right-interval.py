class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start= []
        for i in range(len(intervals)):
            start.append([intervals[i][0],i])
        start.sort()
        ans  =[]
        for i in range(len(intervals)):
            x = intervals[i]
            l = -1
            r = len(start)
            while r - l > 1:
                mid = (l+r)//2
                if start[mid][0] >= x[1]:
                    r = mid
                else:
                    l = mid
            if r >= 0 and r < len(start):
                ans.append(start[r][1])
            else:
                ans.append(-1)
        return ans