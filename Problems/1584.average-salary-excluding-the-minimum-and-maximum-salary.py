# title: Average Salary Excluding the Minimum and Maximum Salary
# timestamp: 2025-06-12 20:43:32
# problemUrl: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)