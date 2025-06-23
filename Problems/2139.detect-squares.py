# title: Detect Squares
# timestamp: 2025-06-23 13:44:59
# problemUrl: https://leetcode.com/problems/detect-squares/
# memory: 19.5 MB
# runtime: 3637 ms

class DetectSquares:

    def __init__(self):
        self.map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.map[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for i in range(1, 1001):
            if (x + i, y + i) in self.map:
                if (x + i, y) in self.map and (x, y + i) in self.map:
                    count += self.map[(x + i, y + i)] * self.map[(x + i, y)] * self.map[(x, y + i)]
            
            if (x - i, y + i) in self.map:
                if (x - i, y) in self.map and (x, y + i) in self.map:
                    count += self.map[(x - i, y + i)] * self.map[(x - i, y)] * self.map[(x, y + i)]

            if (x - i, y - i) in self.map:
                if (x - i, y) in self.map and (x, y - i) in self.map:
                    count += self.map[(x - i, y - i)] * self.map[(x - i, y)] * self.map[(x, y - i)]

            
            if (x + i, y - i) in self.map:
                if (x + i, y) in self.map and (x, y - i) in self.map:
                    count += self.map[(x + i, y - i)] * self.map[(x + i, y)] * self.map[(x, y - i)]

        
        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)