class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        i = 1
        for item in s[::-1]:
            res = (ord(item) - ord("A") + 1) * i + res
            i = i * 26
        return res