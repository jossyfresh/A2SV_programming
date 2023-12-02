class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-(x) for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            large = abs(heapq.heappop(heap))
            small = abs(heapq.heappop(heap))
            if large > small:
                heapq.heappush(heap,-(large-small))
        if heap:
            return abs(heap[0]) 
        else:
            return 0
                
