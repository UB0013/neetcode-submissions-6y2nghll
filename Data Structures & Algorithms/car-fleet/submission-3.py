class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s]for p, s in zip (position,speed)]
        stack =[]
        pairs.sort(reverse=True)
        for i , n in enumerate((pairs)): 
            time = (target- n[0] )/ n[1] 
            stack.append(time)
            if stack and len(stack)>= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)
                    


