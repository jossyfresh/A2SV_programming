class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for x in piles:
            heapq.heappush(heap,-(x))
        for i in range(k):
            x = heapq.heappop(heap)
            x = math.floor(x/2)
            heapq.heappush(heap,x)
        return -1 * sum(heap)