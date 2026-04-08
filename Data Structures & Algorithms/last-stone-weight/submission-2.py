class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1  :
            a = heapq.heappop_max (stones)
            b = heapq.heappop_max(stones)
            res = a-b 
            heapq.heappush_max(stones,res)
        return stones[0]


        