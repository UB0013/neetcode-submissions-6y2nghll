class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r= 0 
        q = collections.deque()
        output = [] 

        for  r in range (len (nums)): 
           
            while q and nums [r] > nums[ q[-1] ] : 
                q.pop()
            q.append (r)

            if q[0] < l:
                q.popleft ( )

            if r-l +1 >= k : 
                output.append(nums[q[0]])
                l = l +1 
           
        return output 
            

        