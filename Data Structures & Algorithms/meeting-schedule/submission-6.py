"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort( key = lambda i : i.start)

        if len(intervals) == 0 :
            return True 
        res = [intervals[0]]
        for i in range (1,len(intervals)):
            if intervals[i].start < res[-1].end : 
                return False 
            else :
                res.append(intervals[i])
        return True 

