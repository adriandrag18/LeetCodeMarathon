# title: Smallest Number in Infinite Set
# timestamp: 2025-01-03 02:16:20
# problemUrl: https://leetcode.com/problems/smallest-number-in-infinite-set/
# memory: 18.6 MB
# runtime: 16 ms

class SmallestInfiniteSet:

    def __init__(self):
        self.bound = 1
        self.set = set()
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            el = heappop(self.heap)
            self.set.remove(el)

            return el
        
        self.bound += 1
        return self.bound - 1

    def addBack(self, num: int) -> None:
        if num >= self.bound or num in self.set:
            return
        
        self.set.add(num)
        heappush(self.heap, num)        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)