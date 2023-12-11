from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        # attempt 2
        # after looking at the solution :😅:
        # https://leetcode.com/problems/jump-game-ii/solutions/18014/concise-o-n-one-loop-java-solution-based-on-greedy/?envType=study-plan-v2&envId=top-interview-150
        hops = 0
        end = 0
        max = 0
        i = 0
        # len - 1 matters, not just len
        while i < len(nums) - 1:
            currentMax = i + nums[i]
            # print(f"[{i}] == end {end}?  currentMax: {currentMax} > {max} ?")
            if currentMax > max:
                max = currentMax
            if i == end:
                hops += 1
                end = max
            i += 1
        return hops
    
        """
        i tried a greedy approach below but it's bugged
        especially with edge cases, probably because it starts from the 2nd element
        """
        # numslen = len(nums)
        # if numslen == 0:
        #     return 0
        
        # current_end = nums[0]
        # hops = 0
        # new_max = nums[0]
        # # new_base = 0
        # i = 1

        # while i <= current_end and i < numslen:
        #     if i + nums[i] >= new_max:
        #         print(f"new_max: {new_max} replaced with: nb: {i} + new_max {nums[i]}")
        #         # new_base = i
        #         new_max = i + nums[i]
        #         # the end is more than or equal to the last index
        #         if new_max > numslen - 1:
        #             print(f"{new_max} > numslen - 1, returning {hops + 1}")
        #             hops += 1
        #             return hops
        #     if i == current_end or i == numslen - 1:
        #         # reached the end of the current possible window
        #         # compute the new longest possible end
        #         print(f"i: {i} currently at current end, new current end: {new_max}")
        #         current_end = new_max
        #         # new_max = new_base + 1
        #         hops += 1
        #         # the end is more than or equal to the last index
        #         if current_end >= numslen - 1:
        #             hops += 1
        #             return hops
        #     i += 1
        # return hops
        

# nums = [2,3,1,1,4]
# print(Solution.jump(Solution, nums))
# nums = [2,3,0,1,4]
# print(Solution.jump(Solution, nums))
# nums = [0]
# print(Solution.jump(Solution, nums))
# nums = [1]
# print(Solution.jump(Solution, nums))
# nums = [2,1]
# print(Solution.jump(Solution, nums))
# nums = [2,1,1,1,4]
# print(Solution.jump(Solution, nums))
# nums = [1,1,1,1]
# print(Solution.jump(Solution, nums))
# nums = [1,2,3]
# print(Solution.jump(Solution, nums))
# nums = [1,2]
# print(Solution.jump(Solution, nums))