# title: Snapshot Array
# timestamp: 2025-06-20 11:48:30
# problemUrl: https://leetcode.com/problems/snapshot-array/
# memory: 42.9 MB
# runtime: 3235 ms

class SnapshotArray:

    def __init__(self, length: int):
        self.maps = [{}]

    def set(self, index: int, val: int) -> None:
        self.maps[-1][index] = val

    def snap(self) -> int:
        self.maps.append({})
        return len(self.maps) - 2

    def get(self, index: int, snap_id: int) -> int:
        for map in reversed(self.maps[:snap_id+1]):
            if index in map:
                return map[index]
        
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)