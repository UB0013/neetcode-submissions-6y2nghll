class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = [] 
        

    def addNum(self, num: int) -> None:
        if self.maxheap and num > self.maxheap[0]:
            heapq.heappush(self.minheap,num)
        else : 
            heapq.heappush_max(self.maxheap,num)
        
        if len(self.maxheap) > len(self.minheap)+1 : 
            move = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap,move)
        if len(self.minheap) > len(self.maxheap)+1 : 
            move = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap,move)
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap): 
            return self.maxheap[0]
        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        else :
            return (self.maxheap[0] + self.minheap[0])/2.0

        
        