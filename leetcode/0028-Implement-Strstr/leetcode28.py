class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        if needle == "":
            return 0
        while i in len(haystack):
            if str[i:i+len(needle)] == needle:
                return i

        return  -1

if __name__ == "__main__":
    