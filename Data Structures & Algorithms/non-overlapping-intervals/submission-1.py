class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = 0  
        prevend = intervals[0][1]
        print (prevend)
        for start, end in intervals[1:] : 
            if start < prevend :
                res += 1
                prevend = min (end,prevend)
            else : 
                prevend = end 
        return res

           


        