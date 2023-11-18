from sortedcontainers import SortedList
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        started = SortedList()
        ended = SortedList()
        for st,en in flowers:
            started.add(st)
            ended.add(en)
        ans = []
        print(started,ended)
        for i in people:
            ind = bisect.bisect_right(started,i)
            indx = bisect.bisect_left(ended,i)
            print(ind,indx)
            print(ind,indx)
            ans.append(ind-indx)
        return ans