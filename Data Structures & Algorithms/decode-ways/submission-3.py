"""`dp[i]` represents the number of ways to decode the first 
`i` characters of the string, so `dp[0] = 1` for the empty string.
 For each position `i` from 2 to n, we check two cases:
  if the last single digit `s[i-1]` is valid (not "0"), 
  we add `dp[i-1]` because we can decode this character alone 
  and inherit all ways to decode the prefix before it;
   if the last two digits `s[i-2:i]` form a valid number between
    "10" and "26", we add `dp[i-2]` because we can decode 
    them together and inherit all ways to decode the prefix 
    before those two. Adding them covers both decoding choices 
    — one-step and two-step — just like climbing stairs. 
    If both checks fail, `dp[i]` stays 0, meaning no valid decoding
     exists for that prefix.
"""


class Solution:
    def numDecodings(self, s: str) -> int:



        n = len (s)
        if n == 0 :
            return 0


        dp = [0] * n 

        dp[0] = 1 if s [0] != "0" else 0 

        for i in range (1,n):
            if s[i] != '0':
                dp[i] = dp[i] + dp[i-1]
            if '10' <= s[i-1:i+1] <= '26':
                if i >= 2:
                    dp[i] += dp[i - 2]
                else:
                    # This handles the very first two-digit pair at the start
                    dp[i] += 1

       
        return dp [n-1]


