# title: Find if Array Can Be Sorted
# timestamp: 2025-05-13 12:52:50
# problemUrl: https://leetcode.com/problems/find-if-array-can-be-sorted/
# memory: 17.9 MB
# runtime: 31 ms

@cache
def countBits(el: int) -> int:
    return el.bit_count()

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        sl = sorted(nums[:])
        for i, (el, sel) in enumerate(zip(nums, sl)):
            print(el, sel)
            if el < sel: 
                continue
            noBits = countBits(el)
            while sl[i] < el:
                if countBits(sl[i]) != noBits:
                    return False
                i += 1
        return True