class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        i=0
        ls=0
        maxc=0
        for j in range(len(s)):
            count[s[j]]=1+count.get(s[j],0)
            maxc=max(maxc,count[s[j]])
            if (j-i+1)-maxc>k:
                count[s[i]]-=1
                i+=1
            ls=max(ls,j-i+1)
        return ls

        