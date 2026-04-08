class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [i for i in count.values()]
        heapq.heapify_max(heap)
        q= deque()
        time = 0 

        while heap or q  : 
            time += 1 
            if heap: 
                x = heapq.heappop_max(heap)-1 
                if x != 0  : 
                    q.append([x,time+n])
            if q and q[0][1] == time : 
                heapq.heappush_max (heap , q.popleft()[0])
        return time 




        print (heap )

        return 0 
        