# title: Construct Smallest Number From DI String
# timestamp: 2025-02-18 21:24:43
# problemUrl: https://leetcode.com/problems/construct-smallest-number-from-di-string/
# memory: 17.8 MB
# runtime: 1 ms

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def helper(li, pattern, remaining):
            if len(remaining) == 0 or pattern == '':
                return li
                
            for n in sorted(list(remaining)):
                if li and ((li[-1] > n and pattern[0] == 'I') or (li[-1] < n and pattern[0] == 'D')):
                    continue
                li.append(n)
                remaining.remove(n)
                res = helper(li, pattern[1:] if len(li) > 1 else pattern, remaining)
                if res: return res
                remaining.add(n)
                li.pop()
        
        remaining = set(range(1, 10))
        return ''.join([str(n) for n in helper([], pattern, remaining)])
