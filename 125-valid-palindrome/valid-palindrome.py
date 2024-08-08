import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=re.sub(r'\W+|_','',s)
        print(s)
        i,j =0,len(s)-1
        for i in range(len(s)):
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            else:
                return False

        return True
        
