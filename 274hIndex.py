# https://leetcode.com/problems/h-index/solutions/70768/java-bucket-sort-o-n-solution-with-detail-explanation
from collections import defaultdict
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort()
        n = len(citations)
        hindexs = [0 for _ in range(n+1)]
        for i in citations:
            if i >= n:
                hindexs[n] += 1
            else: 
                hindexs[i] += 1
        count = 0
        # print(hindexs.items())
        for index in reversed(range(n+1)):
            count += hindexs[index]
            if count >= index:
                return index

        return 0
            
        
            
            


citations = [3,0,6,1,5]
print(Solution.hIndex(Solution, citations), " expected: 3")
citations = [1,3,1]
print(Solution.hIndex(Solution, citations), " expected: 1")
citations = [1,3,1,5,6,7,8,9,1,1,2,3,9,3,4]
print(Solution.hIndex(Solution, citations), " expected: 5")
citations = [0]
print(Solution.hIndex(Solution, citations) , " expected: 0")
citations = [1]
print(Solution.hIndex(Solution, citations) , " expected: 1")
citations = [11,15]
print(Solution.hIndex(Solution, citations) , " expected: 2")
citations = [11,15, 14]
print(Solution.hIndex(Solution, citations) , " expected: 3")
citations = [2, 2, 2]
print(Solution.hIndex(Solution, citations) , " expected: 2")
citations = [4, 4, 0, 0]
print(Solution.hIndex(Solution, citations) , " expected: 2")