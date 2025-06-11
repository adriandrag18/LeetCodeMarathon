# title: Reschedule Meetings for Maximum Free Time I
# timestamp: 2025-02-01 16:56:23
# problemUrl: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/
# memory: 37 MB
# runtime: 59 ms

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        if len(startTime) == 0:
            return eventTime
        
        gaps = [startTime[0] - 0]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])
        print(gaps)
        s = sum(gaps[0:k+1])
        res = s
        for i in range(k+1, len(gaps)):
            s -= gaps[i-k-1]
            s += gaps[i]
            res = max(res, s)
            
        return res