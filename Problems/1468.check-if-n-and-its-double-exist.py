# title: Check If N and Its Double Exist
# timestamp: 2024-12-02 00:20:21
# problemUrl: https://leetcode.com/problems/check-if-n-and-its-double-exist/
# memory: 17.5 MB
# runtime: 0 ms

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or num / 2 in seen:
                return True
            seen.add(num)
        
        return False