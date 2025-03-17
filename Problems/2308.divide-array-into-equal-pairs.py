# title: Divide Array Into Equal Pairs
# timestamp: 2025-03-17 23:16:52
# problemUrl: https://leetcode.com/problems/divide-array-into-equal-pairs/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for n in counter.values():
            if n % 2 == 1:
                return False
        
        return True
        