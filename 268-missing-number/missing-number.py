class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=n*(n+1)//2
        su=sum(nums)
        return s-su
        