# title: Count and Say
# timestamp: 2025-06-22 12:03:02
# problemUrl: https://leetcode.com/problems/count-and-say/
# memory: 17.9 MB
# runtime: 0 ms

dp = ['' for _ in range(30)]

class Solution:
    def countAndSay(self, n: int) -> str:
        if not dp[0]:
            dp[0] = '1'
            for i in range(1, 30):
                s = dp[i-1]
                prev = s[0]
                count = 1
                new = []
                for c in s[1:]:
                    if c == prev:
                        count += 1
                    else:
                        new.append(str(count))
                        new.append(prev)
                        prev = c
                        count = 1
                new.append(str(count))
                new.append(prev)

                dp[i] = ''.join(new)
            
        
        return dp[n-1]