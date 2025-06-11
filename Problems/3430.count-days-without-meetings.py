# title: Count Days Without Meetings
# timestamp: 2025-03-25 16:34:24
# problemUrl: https://leetcode.com/problems/count-days-without-meetings/
# memory: 53.1 MB
# runtime: 133 ms

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        m = 10**10
        meetings.sort(key=lambda x: x[0] * m - x[1])

        res = meetings[0][0] - 1
        currS, currE = meetings[0]
        for s, e in meetings[1:]:
            if currE >= e:
                continue
            
            if currE >= s - 1:
                currE = e
                continue
                
            res += s - currE - 1
            currS, currE = s, e
        
        res += days - currE

        return res