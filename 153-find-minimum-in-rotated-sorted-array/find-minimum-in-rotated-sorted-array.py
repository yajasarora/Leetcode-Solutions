class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        m=r-l//2
        res=nums[0]
        print(m)
        while l<r:
            res=min(nums[m],res)
            if nums[m]>=nums[l] and m<len(nums):
                l=m+1
                m=r-l//2
            else:
                r=m-1
                m=r-l//2
                print(m)
        return res  