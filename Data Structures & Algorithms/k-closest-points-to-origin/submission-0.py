class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap  = [] 
        res =[] 
        for x, y in points : 
            dist = x*x + y*y 
            heap.append([dist,x,y])
        heapq.heapify(heap)
        print (heap)

        while k > 0 : 
            dist, x, y = heapq.heappop(heap)
            res.append ([x,y])
            k  = k -1 
        return res 