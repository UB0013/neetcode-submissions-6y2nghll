class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = sorted(zip(position, speed))

        stack = []
        final = []
       

        for key,value in result : 
            rd = target-key 
            time = rd / value
            stack.append(time)


        final.append(stack[-1])



        for  i in range (len(stack)-1,-1,-1) :
             
            while final and final[-1] < stack[i]:


                final.append(stack[i])

        return len(final)













