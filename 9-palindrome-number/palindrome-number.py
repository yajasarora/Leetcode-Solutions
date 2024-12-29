class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        rev=''
        if "-" in x:
            return False
        else:
            rev+=x[::-1]
            if(x==rev):
                return True
            else:
                return False