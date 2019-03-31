# 超出时间限制
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        # 截取出对应的字符串，再使用python自带的int(num, 2)进行二进制转换
        for i in range(len(A)):
            num = ""
            for x in A[:i+1]:
                num = num+str(x)
            if int(num, 2) % 5==0:
                res.append(True)
            else:
                res.append(False)
        return res