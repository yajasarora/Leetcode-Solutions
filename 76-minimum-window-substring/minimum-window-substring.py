class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count={}
        couns={}
        l=0
        res,reslen=[-1,-1],float("infinity")
        if t=="":
            return ""
        for i in t:
            count[i]=1+count.get(i,0)
            
        have,need=0,len(count)
        for r in range(len(s)):
            couns[s[r]]=1+couns.get(s[r],0)
            if s[r] in count and couns[s[r]]==count[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                couns[s[l]]-=1
                if s[l] in count and couns[s[l]]<count[s[l]]:
                    have-=1 
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('infinity') else ''