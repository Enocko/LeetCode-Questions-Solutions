class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h = defaultdict(int)
        res = ''

        for n in s:
            if (ord('a') - ord(n)) == 0:
                res += n
            
            if res and n not in res:
                res += n
            
            h[n] += 1
    
        return res