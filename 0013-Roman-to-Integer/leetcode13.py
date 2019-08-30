class Solution:
    def romanToInt(self, s: str) -> int:
        dict ={
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        res = 0
        for i in range(len(s)):
            # 判断当前的值是否比前一个大
            if i > 0 and dict[s[i]] > dict[s[i - 1]]:
                # 如果当前值比前一个大则减去
                res += dict[s[i]] - 2 * dict[s[i - 1]]
            else:
                res += dict[s[i]]
        return res

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
