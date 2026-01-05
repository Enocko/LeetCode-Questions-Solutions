class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        cnt = 0

        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digitA + digitB + cnt 
            res = str(total % 2) + res
            cnt = total // 2

        if cnt:
            res = '1' + res
        
        return res