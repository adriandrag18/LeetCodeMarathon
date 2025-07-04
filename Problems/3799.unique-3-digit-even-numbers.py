# title: Unique 3-Digit Even Numbers
# timestamp: 2025-03-15 16:36:11
# problemUrl: https://leetcode.com/problems/unique-3-digit-even-numbers/
# memory: 17.8 MB
# runtime: 19 ms

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k in [i, j] or digits[k] % 2 == 1:
                        continue
                    s.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        # print(sorted(list(s)))
        return len(s)