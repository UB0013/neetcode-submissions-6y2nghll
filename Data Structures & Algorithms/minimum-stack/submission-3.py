class MinStack:
    def __init__(self):
        self.stack = []
        self.stackmin = []
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.stackmin : 
            x = self.stackmin[-1]
            if val < x : 
                self.stackmin.append(val)
            else : 
                self.stackmin.append(x)
        else :
            self.stackmin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]




 








       


       
       
        # for i in self.stack :
        #     if i < m : 
        #         m= i 
        # return m 









        
