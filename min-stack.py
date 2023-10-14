class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_ and self.min_[-1] < val:
            self.min_.append(self.min_[-1])
        else:
            self.min_.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.min_.pop()
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_[-1]
        


            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()