# title: Two Sum II - Input Array Is Sorted
# timestamp: 2024-11-01 21:28:19
# problemUrl: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# memory: 17.6 MB
# runtime: 9 ms

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j < len(numbers):
            el = numbers[j] + numbers[i]
            if el == target:
                return [i + 1, j + 1]
            if el < target:
                i += 1
                continue
            j -= 1
            

        return 0, 0