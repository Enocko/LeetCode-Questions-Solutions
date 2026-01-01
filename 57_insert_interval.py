class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        k = newInterval
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if k[1] < start:
                res.append(k)
                return res + intervals[i:]
            elif k[0] > end:
                res.append(intervals[i])
            else:
                k = [min(k[0], start), max(k[1], end)]
        
        res.append(k)
        return res