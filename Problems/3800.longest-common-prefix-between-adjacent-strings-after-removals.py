# title: Longest Common Prefix Between Adjacent Strings After Removals
# timestamp: 2025-06-29 05:53:29
# problemUrl: https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/
# memory: 40.3 MB
# runtime: 783 ms

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        heap = []
        for i in range(n - 1):
            curr = 0
            for a, b in zip(words[i], words[i+1]):
                if a != b:
                    break
                curr += 1

            heap.append((curr, i))

        heap = nlargest(3, heap)
        heap.append((0, -2))

        res = []
        for i in range(n):
            curr = 0
            for l, j in heap:
                if i in [j, j + 1]:
                    continue
                curr = l
                break
            
            if 0 < i < n - 1:
                count = 0
                for a, b in zip(words[i - 1], words[i+1]):
                    if a != b:
                        break
                    count += 1
                curr = max(curr, count)

            res.append(curr)
                
        return res
                    