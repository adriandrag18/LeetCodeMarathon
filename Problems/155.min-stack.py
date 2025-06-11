# title: Min Stack
# timestamp: 2024-11-07 14:40:10
# problemUrl: https://leetcode.com/problems/min-stack/
# memory: 20.4 MB
# runtime: 7 ms

class MinStack:

    def __init__(self):
        self.stack = []
        # self.minSoFar = []
        self.min = 10000000000

    def push(self, val: int) -> None:
        # self.stack.append(val)
        # if  self.minSoFar:
        #     self.minSoFar.append(min(val, self.minSoFar[-1]))
        # else:
        #     self.minSoFar.append(val)
        self.stack.append(val - self.min)
        self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return
        el = self.stack.pop()
        # self.minSoFar.pop()
        self.min -= 0 if el > 0 else el

    def top(self) -> int:
        if not self.stack:
            return -1
        if self.stack[-1] < 0:
            return self.min
        return self.stack[-1] + self.min

    def getMin(self) -> int:
        if not self.stack:
            return -1
        # return self.minSoFar[-1]
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()