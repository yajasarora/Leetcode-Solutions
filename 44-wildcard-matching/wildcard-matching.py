class Solution(object):
    def isMatch(self, text, pattern):
    
        n = len(pattern)
        m = len(text)
        mem = {}

        def f(n, m):
            if (n, m) in mem:
                return mem[(n, m)]

            # Base cases
            if n == 0 and m == 0:
                mem[(n, m)] = True
            elif n == 0:
                mem[(n, m)] = False
            elif m == 0:
                mem[(n, m)] = all(i == '*' for i in pattern[:n])
            else:
                # If characters match or '?' matches any character
                if pattern[n - 1] == text[m - 1] or pattern[n - 1] == '?':
                    mem[(n, m)] = f(n - 1, m - 1)
                # If '*' matches zero or more characters
                elif pattern[n - 1] == '*':
                    mem[(n, m)] = f(n - 1, m) or f(n, m - 1)
                else:
                    mem[(n, m)] = False
            
            return mem[(n, m)]
        return f(n,m)

