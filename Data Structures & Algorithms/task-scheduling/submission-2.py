class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [i for i in count.values()]
        heapq.heapify_max(heap)
        q = deque ()
        time = 0 

        while heap or q :
            time +=1

            if heap :
                x=heapq.heappop_max(heap)-1
                if x!= 0 : 
                    q.append([time+n,x])
            if q and q[0][0] == time :
                x = q.popleft()
                heapq.heappush_max(heap,x[1])
        return time
        