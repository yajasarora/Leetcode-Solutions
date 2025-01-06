class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i]=nums[j]
                if i!=j:
                    nums[j]=0
                i+=1
