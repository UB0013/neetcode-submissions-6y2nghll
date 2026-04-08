"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [] 
        end = []
        count,res  = 0 , 0 
        for element in intervals :
            start.append(element.start)
            end.append(element.end)
        start.sort ()
        end.sort()
        s, e = 0 , 0 

        while s < (len(intervals)) :
            if start[s] < end[e] :
                s = s+1 
                count = count +1 
            else :
                e= e+1 
                count = count -1 
            res = max(res,count)
        return res 
