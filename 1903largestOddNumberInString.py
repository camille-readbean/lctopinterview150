class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        def isEven(x):
            return x == "0" or x == "2" or x == "4" or x ==  "6" or x == "8"
        
        i = len(num) - 1
        while i >= 0:
            if isEven(num[i]) == False:
                # print(num[:i+1])
                return num[:i+1]
            i -= 1
        return ""
    

nums = "52"
print(Solution.largestOddNumber(Solution, nums))
print(nums)