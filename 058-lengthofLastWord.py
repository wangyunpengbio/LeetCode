class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 直接从后往前找" "，找到停止计数就可以了
        s = s.strip() # 此处的去除末尾空格很关键，因为"a "中的"a"，就算末尾有空格也算是一个单词
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                break
            res = res + 1
            # print(i)
        return res