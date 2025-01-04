class Solution(object):
    def isPalindrome(self, s,i=0):
        s="".join([char.lower() for char in s if char.isalnum()])
        n=len(s)
        def check(i):
            if i>=n//2:
                return True
            if s[i]==s[n-i-1]:
                return check(i+1)
            else:
                return False
        return check(0)