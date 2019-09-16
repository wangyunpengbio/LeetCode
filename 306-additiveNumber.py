class Solution:
    # 深度优先遍历
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(previousNum,num):
            print("***",previousNum,num)
            # 如果还剩两个数字，则直接判断
            if len(num) == 2:
                if previousNum + int(num[0]) == int(num[1]):
                    return True
            for i in range(1,len(num)-1):
                if num[0] == "0" and int(num[:i]) != 0: continue# 防止有数字以0开头
                for j in range(i+1,len(num)+1):
                    print(previousNum,int(num[:i]),int(num[i:j]))
                    if num[i] == "0" and int(num[i:j]) != 0: continue# 防止有数字以0开头
                    if previousNum + int(num[:i]) == int(num[i:j]):
                        if j == len(num):return True # 如果剩下的数字也正好全符合，直接结束
                        if dfs(int(num[:i]),num[i:]):
                            return True
        # 少于3个数字直接False
        if len(num) < 3:return False
        for i in range(1,len(num)):
            print("----------------")
            previousNum = int(num[:i])
            if num[0] == "0" and previousNum != 0: continue# 防止有数字以0开头
            if dfs(previousNum,num[i:]):
                return True
        return False