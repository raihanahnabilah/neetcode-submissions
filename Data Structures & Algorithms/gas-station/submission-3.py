class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # You can do brute force basically
        # n = 4
        # index = 0 -> 1
        # index = 1 -> 2
        # index = 2 -> 3
        # index = 3 -> 0
        
        # j index = n== len() - 1 ? 0 : n + 1


        # But with greedy algo
        # gas -> 
        # station 0 -> tank = 1, cost = 2 -> tank = 1-2 = -1 (cant travel)
        
        # station 1 -> tank = 2, cost = 2 -> tank = 0 (cant travel)

        # station 2 -> tank = 3, cost = 4 -> tank = -1 (cant travel)

        # station 3 -> tank = 4, cost = 1 -> tank = 3
        # station 1 -> tank = 1, cost = 2 -> tank = 3 + 1 - 2 = 2
        # station 2 -> tank = 2, cost = 2 -> tank = 2 + 2 - 2 = 2
        # station 3 -> tank = 4, cost = 1 -> tank = 2 + 4 - 1 = 4

        # To find the index that can start 
        # Greedy algo?
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        storedIndex = 0
        
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]
            total += g - c    

            if total < 0:
                total = 0
                storedIndex = i + 1
        return storedIndex


