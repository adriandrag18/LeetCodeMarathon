# title: 3Sum With Multiplicity
# timestamp: 2025-01-09 16:37:06
# problemUrl: https://leetcode.com/problems/3sum-with-multiplicity/
# memory: 18.1 MB
# runtime: 16 ms

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        nums = arr
        mod = 10**9 + 7
        nums.sort()
        freq = []
        count, last = 1, nums[0]
        for num in nums[1:]:
            if num == last:
                count += 1
                continue
            freq.append((last, count))
            count, last = 1, num
        freq.append((last, count))
        nums = freq
        res = 0
        for i in range(0, len(freq)):
            if 3 * nums[i][0] > target:
                break

            if 3 * nums[i][0] == target and nums[i][1] >= 3:
                res += math.comb(nums[i][1], 3)
                res %= mod
            
            if i + 1 >= len(freq):
                continue
            for j in range(i+1, len(freq)):
                # binary search shoudl have been better here but not worth it
                if 2 * nums[i][0] + nums[j][0] == target:
                    res += math.comb(nums[i][1], 2) * nums[j][1]
                    res %= mod
                if nums[i][0] + 2 * nums[j][0] == target:
                    res += math.comb(nums[j][1], 2) * nums[i][1]
                    res %= mod
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[j][0] + nums[k][0] + nums[i][0]
                if s == target:
                    res += nums[i][1] * nums[j][1] * nums[k][1]
                    res %= mod
                    j += 1
                    k -= 1
                    continue
                
                if s < target:
                    j += 1
                    continue    
                k -= 1
        return res