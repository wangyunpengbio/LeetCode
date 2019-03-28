class Solution:
    # 递归法求解问题
    def letterCombinations(self, digits: str) -> List[str]:
        phoneSet = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        # 如果数字为空，则输出空列表
        if len(digits) != 0:
            # 如果只剩1个数字，则把该数字对应的字母依次加入列表
            if len(digits) != 1:
                # 如果还剩2个数字及以上，则计算后面数字对应的列表，把后面的列表依次怼进第一个数字对应的字母
                addlist = self.letterCombinations(digits[1:])
                res = []
                for i in range(len(addlist)):
                    for j in range(len(phoneSet[digits[0]])):
                        res.append(phoneSet[digits[0]][j] + addlist[i])
                return res
            else:
                res = []
                for letter in phoneSet[digits[0]]:
                    res.append(letter)
                return res
        else:
            return []
