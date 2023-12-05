class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        n = len(nums)
        i = 0
        while i < n:
            if (nums[i] != val):
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
    
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(Solution.removeElement(Solution, nums, val))
# print(nums)