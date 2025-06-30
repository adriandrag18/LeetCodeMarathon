# title: Insert Delete GetRandom O(1)
# timestamp: 2025-06-16 19:33:59
# problemUrl: https://leetcode.com/problems/insert-delete-getrandom-o1/
# memory: 58.2 MB
# runtime: 134 ms

class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        if len(self.arr) == self.map[val] + 1:
            self.arr.pop()
        else:
            self.arr[self.map[val]] = last = self.arr.pop()
            self.map[last]= self.map[val]
        del self.map[val]
        return True

    def getRandom(self) -> int:
        if not self.arr:
            return -1
        rand = random.randint(0, len(self.arr) - 1)
        return self.arr[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()