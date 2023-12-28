from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = [1] * (length + 1)
        right_product = [1] * (length + 1)
        left_accum = 1
        right_accum = 1
        for index, num in enumerate(nums):
            left_accum *= num
            left_product[index+1] = left_accum
        for index, num in enumerate(reversed(nums)):
            right_accum *= num
            right_product[length - index - 1] = right_accum
        # print(f"left prod: {left_product}")
        # print(f"right prod: {right_product}")

        # left have one extra on the right
        # right have one extra on the left
        ans = []
        for i in range(length):
            ans.append(left_product[i] * right_product[i+1])
        return ans


nums = [1,2,3,4]
print(f"ans: {Solution.productExceptSelf(Solution, nums)} expected: [24,12,8,6]")
nums = [-1,1,0,-3,3]
print(f"ans: {Solution.productExceptSelf(Solution, nums)} expected: [0,0,9,0,0]")
