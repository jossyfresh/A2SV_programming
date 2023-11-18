class StockSpanner:

    def __init__(self):
        self.nums = []

    def next(self, price: int) -> int:
        ans = 1
        while self.nums and self.nums[-1][0] <= price:
            val = self.nums.pop()
            ans+=val[1]
        self.nums.append([price,ans])
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)