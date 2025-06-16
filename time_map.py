class TimeMap:

    def __init__(self):
        self.key_to_timestamps = {}
        self.key_and_timestamp_to_value = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_timestamps:
            self.key_to_timestamps[key] = [timestamp]
        else:
            self.key_to_timestamps[key].append(timestamp)
        
        self.key_and_timestamp_to_value[(key, timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_timestamps:
            return ""
        row = self.key_to_timestamps[key]
        if timestamp < row[0]:
            return ""
        l = 0
        r = len(row) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if row[mid] < timestamp:
                l = mid + 1
                res = mid
            elif row[mid] > timestamp:
                r = mid - 1
            else:
                return self.key_and_timestamp_to_value[(key, row[mid])]
        if res < 0:
            return ""
        else:
            return self.key_and_timestamp_to_value[(key, row[res])]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)