# title: Minimum Recolors to Get K Consecutive Black Blocks
# timestamp: 2025-03-08 22:28:34
# problemUrl: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
# memory: 17.7 MB
# runtime: 3 ms

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count, res = 0, 10**9
        r = 0
        for l in range(len(blocks) - k + 1):
            while r - l < k and r <= len(blocks):
                # print(r, blocks[r])
                if blocks[r] == 'W':
                    count += 1
                r += 1
            res = min(res, count)
            if blocks[l] == 'W':
                count -= 1
            # print(l, r, blocks[l:r], count, res)
        
        return res if res != 10**9 else count
        
        