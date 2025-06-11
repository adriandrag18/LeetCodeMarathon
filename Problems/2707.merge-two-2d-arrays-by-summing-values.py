# title: Merge Two 2D Arrays by Summing Values
# timestamp: 2025-03-02 11:45:03
# problemUrl: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# memory: 17.8 MB
# runtime: 1 ms

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        map = {id: val for id, val in nums1}
        for id, val in nums2:
            map[id] = map.get(id, 0) + val
        
        return sorted([[id, val] for id, val in map.items()])
