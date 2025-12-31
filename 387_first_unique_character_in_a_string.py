class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(int)
        for n in s:
            h[n] += 1
        
        for i, n in enumerate(s):
            if h[n] == 1:
                return i
        
        return -1