class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict(int)
        res = 0
        maxf = 0
        l = 0

        for i in range(len(s)):
            h[s[i]] += 1
            maxf = max(maxf, h[s[i]])

            while (i-l+1) - maxf > k:
                h[s[l]] -= 1
                l += 1
            
            res = max(res, i-l+1)
        
        return res