class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r)//2
            time = values[mid][0]
            if time == timestamp:
                return values[mid][1]
            elif time < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if not values:
            return ""
        if values[l-1][0] < timestamp:
            return values[l-1][1]
        else:
            return ""
