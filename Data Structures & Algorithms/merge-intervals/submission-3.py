class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort (key = lambda i : i[0])
        res = []
        res.append(intervals[0])
        for start, end in intervals[1:]:
            if res[-1][1] >= start : 
                res[-1][1] = max (end,res[-1][1])
                #res[-1][0] = min (start,res[-1][0])

            else : 
                res.append([start,end])
                
        return res         