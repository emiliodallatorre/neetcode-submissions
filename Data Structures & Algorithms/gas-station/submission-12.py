class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starting_tanks: list[int] = list(map(lambda cg: cg[0] - cg[1], zip(gas, cost)))
        
        if sum(starting_tanks) < 0:
            return -1
        
        tank: int = 0
        starting: int = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c

            if tank < 0:
                starting = i + 1
                tank = 0
        
        return starting