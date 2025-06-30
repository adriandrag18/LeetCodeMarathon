# title: Maximum Candies You Can Get from Boxes
# timestamp: 2025-06-03 12:55:40
# problemUrl: https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
# memory: 28.3 MB
# runtime: 7 ms

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxesQueue = deque([(box, -1) for box in initialBoxes])
        # opened = set()
        total = 0
        while boxesQueue:
            box, check = boxesQueue.popleft()
            if check == total:
                break
            if not status[box]:
                boxesQueue.append((box, total))
                continue
            # open
            # opened.add(box)
            total += candies[box]
            for key in keys[box]:
                status[key] = 1
            for nextBox in containedBoxes[box]:
                boxesQueue.append((nextBox, -1))
        # print(opened)
        return total