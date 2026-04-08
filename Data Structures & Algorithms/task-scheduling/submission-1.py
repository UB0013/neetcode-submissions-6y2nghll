


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap =  [ i for i in count.values()]
        heapq.heapify_max(heap)
        q = deque()
        time = 0 

        while q or heap : 
            time += 1 
            # reducing its frequescy as the task is being performed now 
            if heap : 
                x = heapq.heappop_max(heap) -1
            #check if the x task is alredy fully completed its schedule 
                if x!= 0 :
                    q.append([x,time+n])
            if q and q[0][1] == time :
                x = q.popleft()
                heapq.heappush_max(heap ,x[0])
        return time 



            

        




        