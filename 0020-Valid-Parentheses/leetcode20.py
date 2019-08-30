class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        # 时间复杂度 o(N^2)
        """
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        return len(s) == 0



    