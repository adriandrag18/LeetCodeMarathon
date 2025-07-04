# title: Online Stock Span
# timestamp: 2025-01-06 15:44:54
# problemUrl: https://leetcode.com/problems/online-stock-span/
# memory: 22.8 MB
# runtime: 57 ms

class StockSpanner:

    def __init__(self):
        self.stack = [(10**9, 0)]

    def next(self, price: int) -> int:
        count = 1
        oldPrice, oldCount = self.stack[-1]
        while price >= oldPrice:
            count += oldCount
            self.stack.pop()
            oldPrice, oldCount = self.stack[-1]
        self.stack.append((price, count))
        return count
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)