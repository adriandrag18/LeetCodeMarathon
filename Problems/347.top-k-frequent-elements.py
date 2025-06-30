# title: Top K Frequent Elements
# timestamp: 2024-10-31 15:30:54
# problemUrl: https://leetcode.com/problems/top-k-frequent-elements/
# memory: 20.3 MB
# runtime: 7 ms

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        
        l = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in l[:k]]
        
        