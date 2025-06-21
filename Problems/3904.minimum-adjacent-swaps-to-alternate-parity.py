# title: Minimum Adjacent Swaps to Alternate Parity
# timestamp: 2025-06-21 19:33:41
# problemUrl: https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/
# memory: 30.5 MB
# runtime: 205 ms

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        countEven = 0
        for num in nums:
            if num & 1 == 0:
                countEven += 1

        if abs(n - 2 * countEven) > 1:
            return -1
            
        countOdds = n - countEven

        count = 0
        swaps = [[], []]
        if n & 1 == 0:
            for i, num in enumerate(nums):
                if i & 1 == num & 1:
                    continue
                if swaps[num & 1]:
                    count += i - swaps[num & 1].pop()
                else:
                    swaps[1 - num & 1].append(i)
            

            count2 = 0
            swaps = [[], []]
            for i, num in enumerate(nums):
                if i & 1 != num & 1:
                    continue
                if swaps[num & 1]:
                    count2 += i - swaps[num & 1].pop()
                else:
                    swaps[1 - num & 1].append(i)
            # print(count, count2)
            return min(count, count2)

        # odds
        if countEven > countOdds:
            for i, num in enumerate(nums):
                if i & 1 == num & 1:
                    continue
                if swaps[num & 1]:
                    count += i - swaps[num & 1].pop()
                else:
                    swaps[1 - num & 1].append(i)

            return count
        
        for i, num in enumerate(nums):
            if i & 1 != num & 1:
                continue
            if swaps[num & 1]:
                count += i - swaps[num & 1].pop()
            else:
                swaps[1 - num & 1].append(i)

        return count
            