class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start_index = 0
        n = len(gas)
        last_stop = -1
        passed = False
        for i in range(n):
            # implement a jump
            if i < last_stop:
                continue

            current_tank = 0
            total_tank = 0
            start_idx = i
            # while not passed:
            # this version is 15 ms faster
            for offset in range(n):
                idx = start_idx + offset
                if idx >= n:
                    idx -= n
                current_tank += gas[idx] - cost[idx]
                if current_tank < 0:
                    last_stop = idx
                    break
                if idx == start_idx:
                    passed = True
            if current_tank >= 0:
                return start_idx
            

        return -1
        # return start_index if total_tank > 0 else -1
