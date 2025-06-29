# title: Random Pick with Weight
# timestamp: 2025-06-29 19:52:25
# problemUrl: https://leetcode.com/problems/random-pick-with-weight/
# memory: 22.7 MB
# runtime: 91 ms

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]
        

    def pickIndex(self) -> int:
        t = random.randint(1, self.w[-1])
        l, r = 0, len(self.w) - 1
        while l <= r:
            m = (l + r) // 2
            if self.w[m] == t:
                return m
            if self.w[m] < t:
                l = m + 1
            else:
                r = m - 1
        
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()