# title: Minimum Index of a Valid Split
# timestamp: 2025-03-27 17:17:23
# problemUrl: https://leetcode.com/problems/minimum-index-of-a-valid-split/
# memory: 35.9 MB
# runtime: 119 ms

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        second = Counter(nums)
        first = {}
        domFirst = [nums[0], 0]
        
        for i, num in enumerate(nums[:-1]):
            first[num] = first.get(num, 0) + 1
            second[num] -= 1

            if num == domFirst[0]:
                domFirst[1] += 1
            elif first[num] > domFirst[1]:
                domFirst = [num, first[num]]

            if domFirst[1] > (i + 1) // 2 and second[domFirst[0]] > (n - i - 1) // 2:
                return i
            
            # print(first, second, domFirst, (i + 1) // 2, (n - i - 1) // 2)
        
        return -1
