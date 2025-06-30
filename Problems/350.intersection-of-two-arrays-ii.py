# title: Intersection of Two Arrays II
# timestamp: 2025-06-21 15:51:58
# problemUrl: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# memory: 17.9 MB
# runtime: 3 ms

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        res = []
        for num, count in Counter(nums2).items():
            for _ in range(min(count, counter.get(num, 0))):
                res.append(num)
        
        return res