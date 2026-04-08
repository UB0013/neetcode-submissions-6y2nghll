class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = length of the LCS between
        #             text1 starting at index i
        #             text2 starting at index j
        #
        # We build this bottom-up, so dp[i][j] depends on:
        #   dp[i+1][j]   -> skipping current char of text1
        #   dp[i][j+1]   -> skipping current char of text2
        #   dp[i+1][j+1] -> using BOTH characters (only valid if they match)

        dp = [[0 for _ in range(len(text2) + 1)] 
                    for _ in range(len(text1) + 1)]

        # Iterate backwards so that dp[i+1][*] and dp[*][j+1]
        # are already computed when we need them
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                # Case 1: characters MATCH
                if text1[i] == text2[j]:
                    # Diagonal represents the best LCS BEFORE both characters.
                    # Since neither character was skipped yet, this is the ONLY
                    # place where we are allowed to add both characters.
                    #
                    # So we extend that previous best by 1.
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # Case 2: characters DO NOT match
                else:
                    # We cannot take both characters.
                    # So we must skip ONE of them and keep the best result.
                    #
                    # dp[i+1][j] -> skip text1[i]
                    # dp[i][j+1] -> skip text2[j]
                    #
                    # We take the maximum because we want the longest result.
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # dp[0][0] represents the LCS of the full strings
        return dp[0][0]
