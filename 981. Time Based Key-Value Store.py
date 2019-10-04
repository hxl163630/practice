from bisect import *


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        insort(self.dic[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        index = bisect_right(self.dic[key], (timestamp, ""))
        if index == 0 and self.dic[key][0][0] > timestamp:
            return ""
        return self.dic[key][index - 1][1]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

kv = TimeMap()

kv.set("foo", "bar", 1)
kv.get("foo", 1)
kv.get("foo", 3)
kv.set("foo", "bar2", 4)
kv.get("foo", 4)
kv.get("foo", 5)