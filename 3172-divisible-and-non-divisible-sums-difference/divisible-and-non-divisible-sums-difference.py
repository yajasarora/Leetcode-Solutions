class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        n1=0
        n2=0
        for i in range(1,n+1):
            if i%m==0:
                n2+=i
            else:
                n1+=i
        return n1-n2
        