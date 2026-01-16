class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend) 
        div = abs(divisor)

        cnt = 0
        while div <= d:
            tmp = div
            mul = 1 
            while d >= tmp:
                d -= tmp
                cnt += mul
                mul += mul
                tmp += tmp
        
        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            cnt = -cnt

        return min(2**31-1, max(-2**31, cnt))