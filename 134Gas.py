"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

 

Constraints:

    n == gas.length == cost.length
    1 <= n <= 105
    0 <= gas[i], cost[i] <= 104


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas =    [  1,  2,  3,  4,  5,  1,  2,  3,  4,  5], 
cost =   [  3,  4,  5,  1,  2,  3,  4,  5,  1,  2]
cuml_gas [  1,  3,  6, 10, 15, 15, ]
cuml_def [ -2, -4, -6, -3,  0, 15, ]
defi     [ -2, -2, -2,  3,  3,  ]
is the solution to just work backwards?
if the solution is unique, its the first positive


gas =       [  2,  3,  4]
cost =      [  3,  4,  3]
defi        [ -1, -1, 1]


"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start_index = 0
        n = len(gas)
        get_index = lambda i: i - n if i >= n else i
        index = 0
        deficit = 0
        highest_surplus = 0
        highest_pos = 0
        while index != n:
            deficit = gas[index] - cost[index]
            if 

        

        return -1
        # return start_index if total_tank > 0 else -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(f"ans: {Solution.canCompleteCircuit(Solution, gas, cost)} expected: 3")
    gas = [2,3,4]
    cost = [3,4,3]
    print(f"ans: {Solution.canCompleteCircuit(Solution, gas, cost)} expected: -1")
