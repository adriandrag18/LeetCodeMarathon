# title: Longest Nice Subarray
# timestamp: 2025-03-18 15:10:24
# problemUrl: https://leetcode.com/problems/longest-nice-subarray/
# memory: 37.1 MB
# runtime: 1898 ms

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        nums = [bin(num)[2:][::-1] for num in nums]
        # print(nums)
        l, res = 0, 1
        bites, duplicates = set(), set()
        for r, num in enumerate(nums):
            for i, el in enumerate(num):
                if el == '0':
                    continue
                if i in bites:
                    duplicates.add(i)
                    continue
                bites.add(i)
            # print(bites, duplicates, l, r)
            
            while duplicates:
                # if l == 0: print(nums[l])
                for i, el in enumerate(nums[l]):
                    # if l == 0: print(i, el)
                    if el == '0':
                        continue
                    if i in duplicates:
                        duplicates.remove(i)
                        continue
                    bites.remove(i)
                    # if l == 0:  print(f'\t {duplicates}')
                l += 1
            res = max(res, r - l + 1)
            # print(bites, duplicates, l, r, res)

        return res