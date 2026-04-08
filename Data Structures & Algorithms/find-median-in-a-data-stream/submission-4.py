class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        heapq.heapify_max(self.maxheap)
        heapq.heapify(self.minheap)
        

    def addNum(self, num: int) -> None:

        if self.maxheap and self.maxheap[0] < num :
            heapq.heappush(self.minheap,num)
        else :
            heapq.heappush_max(self.maxheap,num)

        if len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap,val)
        if len(self.minheap) > len(self.maxheap) +1 :
            val = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap,val)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else :
            return ( (self.maxheap[0]+self.minheap[0])/2.0)
        
        