from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        left, right, l = [], [], SortedList()
        for ele in rating:
            less = l.bisect_left(ele)
            more = len(l) - l.bisect_right(ele)
            l.add(ele)
            left.append([less, more])
        l.clear()
        for ele in rating[::-1]:
            less = l.bisect_left(ele)
            more = len(l) - l.bisect_right(ele)
            l.add(ele)
            right.append([less, more])
        right = right[::-1]
        ans = 0
        for i in range(1, len(rating)-1):
            ans += left[i][0] * right[i][1] + left[i][1] * right[i][0]
        return ans