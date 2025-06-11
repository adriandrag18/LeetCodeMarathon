# title: Time Based Key-Value Store
# timestamp: 2024-12-12 18:34:33
# problemUrl: https://leetcode.com/problems/time-based-key-value-store/
# memory: 73.6 MB
# runtime: 126 ms

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, [])
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        li = self.map.get(key, "")
        l, r = 0, len(li) - 1
        while l <= r:
            m = (l + r) // 2
            if li[m][0] == timestamp:
                return li[m][1]
            if li[m][0] < timestamp:
                l = m + 1
                continue
            r = m - 1
        
        if r == -1:
            return ""
        
        return li[r][1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)