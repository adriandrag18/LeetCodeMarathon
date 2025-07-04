# title: Lemonade Change
# timestamp: 2025-06-12 20:50:19
# problemUrl: https://leetcode.com/problems/lemonade-change/
# memory: 21.9 MB
# runtime: 4 ms

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1
                continue
            elif bill == 10:
                tens += 1
                fives -= 1
            elif tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3

            if fives < 0:
                return False
        
        return True