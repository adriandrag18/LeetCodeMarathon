# title: Letter Combinations of a Phone Number
# timestamp: 2024-12-30 16:35:22
# problemUrl: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# memory: 17.3 MB
# runtime: 0 ms

class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno", 
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz"
        }
        res = []

        def helper(digits, li):
            if len(li) == len(digits):
                res.append(li)
                return
                
            for i in map[digits[len(li)]]:
                helper(digits, li + i)
        
        helper(digits, '')
        return res
            
