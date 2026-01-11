class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = ''
        
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m > num:
                r = m - 1
            else:
                res = m
                l = m + 1
        
        return res * res == num