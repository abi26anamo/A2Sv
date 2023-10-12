class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        total_gas = 0
        total_cost = 0
        n = len(gas)

        for i in range(n):
            total_gas+=gas[i]
            total_cost+=cost[i]  

            tank+= gas[i]-cost[i] 

            if tank <0:
                start = i+1
                tank = 0 

        if total_gas>=total_cost:
            return start
        return -1
