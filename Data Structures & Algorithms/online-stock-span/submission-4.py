class StockSpanner:

    def __init__(self):
        self.stack =[] 
        self.count = -1
    def next(self, price: int) -> int:

        self.count += 1 
        result =1 

        # if not self.stack :
        #     self.stack.append([self.count,price])
        #     return self.count+1

        while self.stack and self.stack[-1][1] <= price :
            idx, val = self.stack.pop()
            #result = (self.count - idx)+1

        result = self.count - self.stack[-1][0] if self.stack else self.count + 1
        self.stack.append([self.count,price])
        return result 



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)