class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 头尾指针的双向遍历
        i,j = 0,len(s)-1
        while(i<j):
            # 判断是否是数字和字母
            if not (65<= ord(s[i]) <=90 or 97<= ord(s[i]) <=122 or 48<= ord(s[i]) <=57):
                i = i + 1
                continue
            if not (65<= ord(s[j]) <=90 or 97<= ord(s[j]) <=122 or 48<= ord(s[j]) <=57):
                j = j - 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i = i + 1
            j = j - 1
        return True