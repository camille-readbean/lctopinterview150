from collections import defaultdict, deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # all substring candidates will be from 0 to n/k
        # since the longest substring can only be n/k since n' * k = n
        # at most, where n' is length of substring
        # find all candidates
        a_cnt = defaultdict(lambda: 0)
        for i in s:
            a_cnt[i] = a_cnt[i] + 1
        # viable have to be k count or multiples of k
        viable_a = {}
        for a in a_cnt.keys():
            if a_cnt[a] % k == 0:
                viable_a[a] = a_cnt[a]
        
        # do BFS and find largest longest
        q = deque( reverse(sorted( viable_a.keys() )) )
        while q:
            cur = q.popleft()

    def get_neighbours(s, chars: dict) -> [string], dict:
        for a in reversed(sorted(chars.keys())):
            if chars[a] > 0:
                chars[a] -= 1
                
