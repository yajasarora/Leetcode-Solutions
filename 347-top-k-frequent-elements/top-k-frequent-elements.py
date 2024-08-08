class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        j={}
        c=[]
        for i in nums:
            if i not in j:
                j[i]=0
            else:
                j[i]+=1
        
        j=sorted(j.items(),key=lambda x:x[1],reverse=True)
        for i in j:
            if k==0:
                return c
            c.append(i[0])
            k-=1
        return c