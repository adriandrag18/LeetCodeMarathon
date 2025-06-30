# title: Take Gifts From the Richest Pile
# timestamp: 2024-12-12 12:22:38
# problemUrl: https://leetcode.com/problems/take-gifts-from-the-richest-pile/
# memory: 17.3 MB
# runtime: 277 ms

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            i = max(range(len(gifts)), key=lambda i: gifts[i])
            gifts[i] = int(sqrt(gifts[i]))
        
        
        return sum(gifts)