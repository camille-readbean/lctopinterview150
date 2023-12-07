from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # default dict introduces a speed up by
        # ~20 ms, enough to go from 8.60% of Python users to
        # 72.68% of Python users
        seen = defaultdict(int)
        mostSeen = nums[0]
        mostSeenCount = 0
        for i in nums:
            # if i not in seen.keys():
            #     seen[i] = 1
            # else:
            #     # seen[i] = seen[i] + 1
            seen[i] += 1
            if seen[i] > mostSeenCount:
                mostSeenCount = seen[i]
                mostSeen = i

        return mostSeen


# nums = [2,2,1,1,1,2,2]
# print(Solution.majorityElement(Solution, nums))
# print(nums)