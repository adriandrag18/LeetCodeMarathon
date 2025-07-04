# title: Substring with Concatenation of All Words
# timestamp: 2025-06-16 17:32:41
# problemUrl: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# memory: 20 MB
# runtime: 24 ms

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m, l = len(s), len(words), len(words[0])
        map = {}
        for i, w in enumerate(words):
            if w not in map:
                map[w] = []
            map[w].append(i)

        arr = [(-1, -1)] * n
        for i in range(n - l + 1):
            if s[i:i+l] in map:
                arr[i] = (map[s[i:i+l]][0], len(map[s[i:i+l]]))
        # print(arr)
        all = len(map)

        res = []
        for left in range(l):  
            window = [0] * m
            have = 0
            right = left
            while right < n:
                el, need = arr[right]
                if el != -1:
                    window[el] += 1
                    if window[el] == need:
                        have += 1
                right += l

                if right - left == m * l:
                    if have == all:
                        res.append(left)
                    
                    el, need = arr[left]
                    if el != -1:
                        if window[el] == need:
                            have -= 1
                        window[el] -= 1
                    left += l

        return res