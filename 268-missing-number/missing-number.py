class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=n*(n+1)//2
        for i in nums:
            s-=i
        return s
        