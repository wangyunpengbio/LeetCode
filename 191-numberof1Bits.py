class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        n = str(n)
        print(n)
        for item in n:
            if item == "1":
                res = res + 1
        return res
        # 用1当做mask进行位运算 + 移位运算
        # res = 0
        # while n != 0:
        #     res = res + (n & 1)
        #     # print(res,n & 1)
        #     n = n >> 1
        # return res