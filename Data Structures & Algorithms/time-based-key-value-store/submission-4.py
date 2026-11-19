class TimeMap:
    vals: dict[str, list[str]]
    timestamps: dict[str, list[int]]

    def __init__(self):
        self.vals = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.vals:
            self.vals[key] = [value]
            self.timestamps[key] = [timestamp]
        else:
            self.vals[key].append(value)
            self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals or timestamp < self.timestamps[key][0]:
            return ""

        timestamps: list[int] = self.timestamps[key]

        l, r = 0, len(timestamps)

        def get_m(l: int, r: int) -> int:
            return (r - l) // 2 + l

        while l < r - 1:
            if timestamps[get_m(l, r)] > timestamp:
                r = get_m(l, r)
            else:
                l = get_m(l, r)
        
        return self.vals[key][l]
