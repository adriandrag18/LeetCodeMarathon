# title: Defuse the Bomb
# timestamp: 2024-11-18 02:43:28
# problemUrl: https://leetcode.com/problems/defuse-the-bomb/
# memory: 16.8 MB
# runtime: 0 ms

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]
        
        res = [0] * len(code)
        i, s = 0, sum(code[1:k+1])
        # res[0] = s
        while i < len(code):
            res[i] = s
            i += 1
            s += code[(i+k)%len(code)]
            s -= code[(i)%len(code)]
        
        return res