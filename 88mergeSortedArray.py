class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        li = 0
        loffset = 0
        ri = 0
        # i = 0
        if len(nums2) == 0:
            return
        while li < m and ri < n:
            # print(f"comparing nums1[{li + loffset}] {nums1[li + loffset]} and nums2[{ri}] {nums2[ri]}")
            if nums1[li + loffset] >= nums2[ri]:
                e = li + loffset
                t = m+n-1
                # print(f"e: {li+loffset} t: {m+n-1}")
                while t > e:
                    # print(f"nums1[t] ({nums1[t]}) = nums1[t-1] ({nums1[t-1]})")
                    nums1[t] = nums1[t-1]
                    t -= 1
                # print(f"nums1[li + loffset] ({nums1[li + loffset]}) = nums1[li + loffset] ({nums1[li + loffset]})")
                nums1[li + loffset] = nums2[ri]
                ri += 1
                loffset += 1
            else:
                li += 1
        while ri < n:
            # print(f"Adding  nums2[{ri}] ({nums2[ri]}) to nums1[{li+loffset}]")
            nums1[li+loffset] = nums2[ri]
            ri += 1
            li += 1



# print("1:")
# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3
# Solution.merge(Solution, nums1, m, nums2, n)
# print(nums1)

# print("2:")
# nums1=[1]
# m=1
# nums2=[]
# n=0
# Solution.merge(Solution, nums1, m, nums2, n)
# print(nums1)

# print("3:")
# nums1=[0]
# m=0
# nums2=[1]
# n=1
# Solution.merge(Solution, nums1, m, nums2, n)
# print(nums1)

print("4:")
nums1=[2,0]
m=1
nums2=[1]
n=1
Solution.merge(Solution, nums1, m, nums2, n)
print(nums1)