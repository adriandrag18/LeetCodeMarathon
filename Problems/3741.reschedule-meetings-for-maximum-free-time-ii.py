# title: Reschedule Meetings for Maximum Free Time II
# timestamp: 2025-02-01 17:33:29
# problemUrl: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/
# memory: 47.4 MB
# runtime: 416 ms

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        if len(startTime) == 0:
            return eventTime
        
        gaps = [(startTime[0] - 0, endTime[0] - startTime[0])]
        for i in range(1, len(startTime)):
            gaps.append((startTime[i] - endTime[i-1], endTime[i] - startTime[i]))
        gaps.append((eventTime - endTime[-1], -1))
        
        print(gaps)
        topGaps = sorted([el[0] for el in gaps], reverse=True)[0:3]
        print(topGaps)
        
        res = 0
        for i in range(len(gaps) - 1):
            gap, interval = gaps[i]
            nextGap = gaps[i+1][0]
            res = max(res, gap + nextGap)
            
            maxGap = topGaps[0]
            if maxGap in [gap, nextGap]:
                maxGap = topGaps[1]
            if ( nextGap == topGaps[1] and gap == topGaps[0] ) or ( nextGap == topGaps[0] and gap == topGaps[1] ):
                maxGap = topGaps[2]

            # print(i, gaps[i+1][0], gap, interval, nextGap, maxGap, res)
            if interval <= maxGap:
                res = max(res, gap + nextGap + interval)
                print(res)
            
        return res