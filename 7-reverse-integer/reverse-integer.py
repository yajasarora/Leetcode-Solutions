
class Solution(object):
    def reverse(self, x):
        a=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while (x!=0):
            a*=10
            a+=(x%10)
            x//=10
            if a>(2**31)-1:
                return 0
        return sign*a
        