
from typing import List
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans =[]
        for i in nums :
            freq[i] =  1 + freq.get(i,0) 

        for key, value in freq.items():
            if len(ans)< k :
              #changed key, value to value ,key as the sorting in heap is done based on 1st element

                heapq.heappush(ans,[value,key])
            else:
              # pushpop removes the least value and replaces it with a larger value
                heapq.heappushpop(ans,[value,key])
        return [key  for value,key in ans ]

        



        
      