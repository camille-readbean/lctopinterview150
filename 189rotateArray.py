from copy import deepcopy

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        
        ## Deep copy solution
        # temp_nums = deepcopy(nums)
        # n = len(nums)

        # def newIndex(i):
        #     return (i + k) % n
        # for i in range(n):
        #     nums[newIndex(i)] = temp_nums[i]

        ## "Recursive but TLE"
        # n = len(nums)
        # temp = nums[n-1]
        # i = n-1
        # # while i > 0:
        # #     nums[i] = nums[i-1]
        # #     i -= 1
        # nums = nums[0:n-1]
        # nums = [temp] + nums

        # Solution.rotate(self, nums, k-1)

        ## Reverse and reverse reverse
        ## 
        # https://leetcode.com/problems/rotate-array/solutions/2981122/o-1-space-100-pass-python-with-comments-explanation-two-pointer-rotate-array/
        # 
        # Input: nums = [1,2,3,4,5,6,7], k = 3
        # rotate 3 steps to the right: [5,6,7,1,2,3,4]
        #                                   ^
        # Reverse: [7, 6, 5, 4, 3, 2, 1]
        # Split at 3, reverse each section
        # left: [5, 6, 7, 4 ,3, 2, 1]
        # Now reverse the right side too
        # [5, 6, 7, 1, 2, 3, 4]
        #
        # Input: nums = [1,2], k = 3
        # rotate 3 steps: [2, 1]
        # same as rotating 3 % 2 = 1 time

        if k > len(nums):
            k = k % len(nums)

        nums.reverse()

        i = 0
        split = k - 1

        # print(nums)
        while i < split:
            nums[i], nums[split] = nums[split], nums[i]
            i +=1
            split -=1
        
        split = k
        end = len(nums) - 1

        while split < end:
            nums[split], nums[end] = nums[end], nums[split]
            split +=1
            end -=1



        

# nums = [1,2,3,4,5,6,7]
# print(Solution.rotate(Solution, nums, 3))
# print(nums)