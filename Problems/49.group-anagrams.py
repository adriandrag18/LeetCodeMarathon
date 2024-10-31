# title: Group Anagrams
# timestamp: 2024-10-31 15:20:28
# problemUrl: https://leetcode.com/problems/group-anagrams/
# memory: 19.9 MB
# runtime: 11 ms

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ss = ''.join(sorted(s))
            d[ss] = d.get(ss, [])
            d[ss].append(s)
        
        res = []
        for sett in d.values():
            res.append(sett)
        
        return res