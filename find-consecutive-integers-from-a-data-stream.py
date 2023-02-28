class DataStream:

    def __init__(self, value: int, k: int):
        self.datastream = []
        self.val = value
        self.n = k
        self.k = self.n
    def consec(self, num: int) -> bool:
        if num == self.val:
            self.n-=1
            self.datastream.append(num)
        else:
            self.n = self.k
            self.datastream.append(num)
        if self.n <= 0:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)