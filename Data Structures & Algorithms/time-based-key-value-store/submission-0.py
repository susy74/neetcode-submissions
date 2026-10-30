class TimeMap:

    def __init__(self):
        self.cache = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        v = self.cache.get(key, [])
        l = 0
        r = len(v) - 1
        while l <= r:
            mid = (r + l) // 2
            if v[mid][1] <= timestamp:
                res = v[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


        
