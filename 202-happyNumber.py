class Solution:
    def isHappy(self, n: int) -> bool:
        # 用一个集合来防止循环重复，遇到等于1就可以直接返回True
        alreadyMeet = set()
        def calculateSUM(n):
            res = 0
            while n > 0 :
                n,curNum = divmod(n,10)
                res += curNum ** 2
            return res
        while n not in alreadyMeet:
            alreadyMeet.add(n)
            if n == 1:return True
            n = calculateSUM(n)
        return False