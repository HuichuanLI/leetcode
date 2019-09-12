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




class Solution:
    def isValid(self, s):
        leftP = "([{"
        rightP = ")]}"
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []