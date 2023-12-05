class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        n = len(nums)
        i = 1
        val = nums[0] 
        while i < n:
            if (nums[i] != val):
                nums[k] = nums[i]
                k += 1
                val = nums[i]
            i += 1
        return k
    

# nums = [0,0,1,1,1,2,2,3,3,4]
# print(Solution.removeDuplicates(Solution, nums))
# print(nums)