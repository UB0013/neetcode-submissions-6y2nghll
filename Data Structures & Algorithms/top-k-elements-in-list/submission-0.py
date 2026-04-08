from typing import List
import heapq 
# {3: 18 , 4 : 13}


from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict (int)
        result = []

        for i in nums : 
            freq[i] = 1 + freq.get(i, 0)

        for key, value in freq.items(): 
            if len(result)< k: 
                heapq.heappush( result,[value,key])
            else : 
                heapq.heappushpop(result,[value,key])
        
        return [key for value,key  in result ] 
        

        
  