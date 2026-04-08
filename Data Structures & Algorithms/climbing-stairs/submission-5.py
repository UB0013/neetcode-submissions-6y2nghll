"""

DP Solution (Bottom-Up)
Step 1: Define State

Let dp[i] = number of ways to reach step i.

Step 2: Base Cases (Why)

dp[0] = 1 → There’s one way to stand still at ground.

dp[1] = 1 → Only one way to reach first step (just take 1 step).

Step 3: Build Relation (Why)

To reach step i:

You could come from step i-1 (1 step jump)

Or from step i-2 (2 step jump)

So:

dp[i] = dp[i-1] + dp[i-2]


This ensures we count all unique paths to step i.

Step 4: Fill Table

Go from step 2 to n and apply formula.

Step 5: Answer

Return dp[n], which is the total ways to reach top.

"""


""""SELF EXPL :  
At every index
I am checking the different ways one can reach that index
so for index i , ways to reach is one step before [i-1]  + two steps before [i-2]"""

class Solution:
    
    def climbStairs(self, n: int) -> int:
        dp = [0]* (n+1) 
        def dpp (n): 
            if n== 0 :
                return 0
            dp[0] = 1
            for i in range (1,n+1):
                # a small check so that index is not out of range
                # if we do not want this check we can initialise 
                #dp[1] = 1 
                # since the way to reach i = 1 is only 1 way 
                if (i -1 ) >= 0 and (i-2) >=0 :
                    
                    dp [i] = dp[i-1] + dp [i-2]
                else : 
                    dp[i]= 1 
            return dp[n]
        result =  dpp (n)
        return result 
                
            


