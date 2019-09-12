class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False;
        x = str(x)
        i = 0
        j = len(x) - 1
        while (i < j):
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True


# 时间复杂度: O(N) 空间复杂度: O(N)
# 这道题目还是比较简单的，我们先来看下代码的执行流程： 判断 x 是否为负数，如果是负数直接返回；
# 反转 x , 如果反转之后的值与原来的值不同直接返回 false；
# 如果不为负数，同时与反转后的值相等则返回 true。 下面来看下具体的代码：
# solution2 就是真的反转一下和原来的值进行对比
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数肯定不是palindrome
        # 如果一个数字是一个正数，并且能被10整除，那它肯定也不是palindrome，因为首位肯定不是0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev, y = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return y == rev


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
