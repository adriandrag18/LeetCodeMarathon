# title: Find Longest Special Substring That Occurs Thrice I
# timestamp: 2025-01-02 13:17:03
# problemUrl: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
# memory: 17.9 MB
# runtime: 6 ms

class Solution:
    def maximumLength(self, s: str) -> int:
        curr, n = '', 0
        map = {}
        for c in s:
            if not curr:
                curr, n = c, 1
                continue
            if curr == c:
                n += 1
                continue
            subStr, subStr1, subStr2 = curr * n, curr * (n - 1), curr * (n - 2)
            # print(curr, n, subStr)
            map[subStr] = map.get(subStr, 0) + 1
            map[subStr1] = map.get(subStr1, 0) + 2
            map[subStr2] = map.get(subStr2, 0) + 3
            curr, n = c, 1
        # print(curr, n)
        if curr:
            subStr, subStr1, subStr2 = curr * n, curr * (n - 1), curr * (n - 2)
            map[subStr] = map.get(subStr, 0) + 1
            map[subStr1] = map.get(subStr1, 0) + 2
            map[subStr2] = map.get(subStr2, 0) + 3
        # print(map)

        res, m = -1, -1
        for subStr, count in map.items():
            if count >= 3:
                res = max(res, len(subStr))

        return res if res else -1


        