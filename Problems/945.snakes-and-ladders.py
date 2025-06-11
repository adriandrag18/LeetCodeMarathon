# title: Snakes and Ladders
# timestamp: 2025-06-05 14:29:03
# problemUrl: https://leetcode.com/problems/snakes-and-ladders/
# memory: 17.9 MB
# runtime: 15 ms

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n**2
        def b(i):
            if i >= target:
                return target
            x, y = divmod(i - 1, n)
            if x % 2 == 1:
                y = n - 1 - y
            x = n - 1 - x
            return board[x][y] if board[x][y] != -1 else i
        
        seen = set([1])
        queue = deque([(1, 0)])
        while queue:
            pos, no = queue.popleft()
            for i in range(6, 0, -1):
                next = b(pos + i)
                if next == target:
                    return no + 1
                if next in seen:
                    continue
                seen.add(next)
                queue.append((next, no + 1))
        
        return -1

        