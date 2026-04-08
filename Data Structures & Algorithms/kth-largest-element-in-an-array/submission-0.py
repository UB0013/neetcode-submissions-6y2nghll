class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify_max(nums)
        print(nums)

        while k > 0 : 
            res = heapq.heappop_max(nums)
            k = k-1 
        
        return res 

        