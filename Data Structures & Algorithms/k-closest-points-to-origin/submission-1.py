class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        output =[]

        for x, y  in points : 
            dist = x*x + y*y
            heapq.heappush(res,[dist,[x,y]])
        
        while k > 0 :
            final, cord = heapq.heappop(res)
            output.append(cord)
            k = k -1 
        return output 





        