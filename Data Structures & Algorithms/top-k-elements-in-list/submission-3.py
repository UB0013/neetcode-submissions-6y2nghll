class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for n in nums :
            freq[n] = 1+ freq.get (n, 0)
        print(freq)
        for key, value in freq.items () : 
            if len(ans) < k :
                heapq.heappush(ans, [value,key])
            else :
                heapq.heappushpop(ans,[value,key])

        return [key for [value,key] in ans]
        


        