class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mwater=0
        l,r=0,len(height)-1
        while l<r:
            if min(height[l],height[r])*(r-l)>mwater:
                mwater=min(height[l],height[r])*(r-l)
            if height[l]>=height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
        print(height[r],height[l])
        return mwater

