"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
    
        if not intervals:
            return 0

        intervals.sort(key=lambda i: i.start)
        heap = []  # min-heap of end times

        for meeting in intervals:
            if heap and heap[0] <= meeting.start:
                heapq.heappop(heap)   # room freed
            heapq.heappush(heap, meeting.end)

        return len(heap)

