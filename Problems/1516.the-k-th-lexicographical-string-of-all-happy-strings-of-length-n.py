# title: The k-th Lexicographical String of All Happy Strings of Length n
# timestamp: 2025-02-19 11:34:46
# problemUrl: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# memory: 17.8 MB
# runtime: 3 ms

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def helper(li):
            # print(li)
            nonlocal n, k, count
            if len(li) == n:
                count += 1
                if count == k:
                    return li
                return 
                
            for l in 'abc':
                if li and li[-1] == l:
                    continue
                
                li.append(l)
                res = helper(li)
                if res: return res
                li.pop()
        
        count = 0
        res = helper([])
        # print(res)
        return ''.join(res) if res else ''