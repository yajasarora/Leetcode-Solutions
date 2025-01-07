class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consec=0
        count=0
        for i in nums:
            if i==0:
                consec=max(consec,count)
                count=0
                continue
            count+=1
        consec=max(count,consec)
        return consec