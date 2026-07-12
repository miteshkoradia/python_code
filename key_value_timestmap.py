from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        self.key_value_timestamp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_value_timestamp:
            self.key_value_timestamp[key] = SortedDict()

        self.key_value_timestamp[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value_timestamp:
            return ""
        
        it = self.key_value_timestamp[key].bisect_right(timestamp)

        if it == 0:
            return ""

        return self.key_value_timestamp[key].peekitem(it - 1)[1] 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)


def main():
    ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    args = [
        [],
        ["foo", "bar", 1],
        ["foo", 1],
        ["foo", 3],
        ["foo", "bar2", 4],
        ["foo", 4],
        ["foo", 5],
    ]

    results = [None]
    time_map = TimeMap()

    for op, arg in zip(ops[1:], args[1:]):
        method = getattr(time_map, op)
        results.append(method(*arg))

    print(results)




if __name__ == "__main__":
    main()

