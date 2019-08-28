class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0 :
            sign = -1
            x = - x
        res = 0
        while x:
            res = res*10 + x % 10
            x = x // 10
            if res < 0:
                return 0
        return sign*res if res <= 0x7fffffff else 0