class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        q = []
        res = []

        for i in nums : 
            freq[i] = 1 + freq.get(i, 0)

    
        
        for value ,frq  in freq.items() : 
            if len(q) < k: 
                heapq.heappush(q, (frq,value))
            elif len(q)>= k :
                heapq.heappushpop(q,(frq,value))


        for frq, value in q :
            res.append(value)

        return res 



        

