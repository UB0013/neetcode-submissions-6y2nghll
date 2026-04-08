class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        arr = []

        for n in tokens : 
            if n == '+':
                arr.append(arr.pop()+ arr.pop())
            elif n == '-':
                a= arr.pop()
                b= arr.pop()
                arr.append(b-a)
            elif n == '*':
                arr.append(arr.pop()* arr.pop())
            elif n == '/':
                a= arr.pop()
                b= arr.pop()
                arr.append(int(b/a))
            else:
                arr.append(int(n))

        return arr[0]





        

     

       