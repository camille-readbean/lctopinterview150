# https://leetcode.com/problems/jump-game/submissions/1117098305?envType=study-plan-v2&envId=top-interview-150
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max = nums[0]
        i = 0
        end = len(nums) - 1
        while i < end+1:
            if i <= max:
                new_max = nums[i] + i
                # print(f"{i}: new_max: {new_max}")
                if new_max >= end:
                    return True
                if new_max > max:
                    max = new_max
            i += 1
        return False

        

# nums = [2,3,1,1,4]
# print(Solution.canJump(Solution, nums))
# nums = [3,2,1,0,4]
# print(Solution.canJump(Solution, nums))
# nums = [0]
# print(Solution.canJump(Solution, nums))