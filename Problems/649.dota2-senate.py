# title: Dota2 Senate
# timestamp: 2024-12-30 13:10:03
# problemUrl: https://leetcode.com/problems/dota2-senate/
# memory: 18.6 MB
# runtime: 16 ms

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiants = [i for i, s in enumerate(senate) if s == 'R']
        dires = [i for i, s in enumerate(senate) if s == 'D']
        
        i = 0
        while i < len(radiants) and i < len(dires):
            if radiants[i] < dires[i]:
                radiants.append(n)
            else:
                dires.append(n)
            n += 1
            i += 1
            # dires = dires[1:]
            # radiants = radiants[1:]
        
        return 'Dire' if i < len(dires)  else 'Radiant'
            
                