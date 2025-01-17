class Solution(object):
    def isMatch(self, text, pattern):
    
        n = len(pattern)
        m = len(text)
        dp=[[False]*(m+1) for _ in range(n+1)]

        dp[0][0]=True
        for i in range(1,n+1):
            if pattern[i-1]=='*':
                dp[i][0]=dp[i-1][0]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if pattern[i-1] == text[j-1] or pattern[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                # If '*' matches zero or more characters
                elif pattern[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[n][m]


        # def f(n, m):
        #     if (n, m) in mem:
        #         return mem[(n, m)]

        #     # Base cases
        #     if n == 0 and m == 0:
        #         mem[(n, m)] = True
        #     elif n == 0:
        #         mem[(n, m)] = False
        #     elif m == 0:
        #         mem[(n, m)] = all(i == '*' for i in pattern[:n])
        #     else:
        #         # If characters match or '?' matches any character
        #         if pattern[n - 1] == text[m - 1] or pattern[n - 1] == '?':
        #             mem[(n, m)] = f(n - 1, m - 1)
        #         # If '*' matches zero or more characters
        #         elif pattern[n - 1] == '*':
        #             mem[(n, m)] = f(n - 1, m) or f(n, m - 1)
        #         else:
        #             mem[(n, m)] = False
            
        #     return mem[(n, m)]
        # return f(n,m)

