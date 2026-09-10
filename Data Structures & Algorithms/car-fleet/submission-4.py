class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed)))

        arrival_times: list[float] = list(map(lambda ps: (target - ps[0]) / ps[1], zip(position, speed)))
        heap: list[float] = []

        bursts: int = 0
        last_time: float = -1.0
        for arrival_time in reversed(arrival_times):
            if arrival_time > last_time:
                bursts += 1
                last_time = arrival_time
            
        return bursts