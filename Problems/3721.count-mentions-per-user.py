# title: Count Mentions Per User
# timestamp: 2025-01-31 15:15:02
# problemUrl: https://leetcode.com/problems/count-mentions-per-user/
# memory: 18.2 MB
# runtime: 40 ms

class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        offline = [[] for _ in range(n)]
        for event in events:
            if event[0] != "OFFLINE":
                continue
            
            id, time = int(event[2]), int(event[1])
            offline[id].append((time, time + 60))
        
        all = 0
        res = [0 for _ in range(n)]
        for event in events:
            if event[0] != "MESSAGE":
                continue

            time, mentions = int(event[1]), event[2]

            for mention in mentions.split():
                if mention[:2] == "id":
                    id = (int(mention[2:]))
                    res[id] += 1
                    continue

                all += 1
                if mention == "ALL":
                    continue
                    
                for id in range(n):
                    for interval in offline[id]:
                        if interval[0] <= time < interval[1]:
                            res[id] -= 1
                            break

        for id in range(n):
            res[id] += all
        
        return res
