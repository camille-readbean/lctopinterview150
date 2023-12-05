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
        appeared = 1
        while i < n:
            if (nums[i] != val):
                # print(f"switching at k:{k} to nums[i] {nums[i]}")
                nums[k] = nums[i]
                k += 1
                val = nums[i]
                appeared = 1
            elif (nums[i] == val and appeared < 2):
                # print(f"i: {i} k: {k} val: {val}")
                nums[k] = nums[i]
                appeared += 1
                k += 1
            i += 1
        return k


# nums = [0,0,1,1,1,1,2,3,3]
# print(Solution.removeDuplicates(Solution, nums))
# print(nums)