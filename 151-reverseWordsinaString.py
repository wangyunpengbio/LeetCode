class Solution:
    # 直接split默认是去掉空字符串
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])