class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r)//2
            time = values[mid][0]
            if time <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
