class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        map={')':'(','}':'{',']':'['}

        for i in s:
            if stack and i in map and stack[-1]==map[i]:
                stack.pop()
            else:
                stack.append(i)
        return not stack
        


            
        