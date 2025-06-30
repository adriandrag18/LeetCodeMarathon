# title: Richest Customer Wealth
# timestamp: 2025-06-12 22:13:48
# problemUrl: https://leetcode.com/problems/richest-customer-wealth/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(banks) for banks in accounts])