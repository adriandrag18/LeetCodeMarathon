# title: Generate Tag for Video Caption
# timestamp: 2025-06-21 17:35:13
# problemUrl: https://leetcode.com/problems/generate-tag-for-video-caption/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def generateTag(self, caption: str) -> str:
        res = ['#']
        caption.strip()
        upper = False
        for c in caption:
            if c.isalpha():
                if upper:
                    upper = False
                    res.append(c.upper())
                else:
                    res.append(c.lower())
            elif c == ' ' and len(res) > 1:
                upper = True

        return ''.join(res[:100])
            