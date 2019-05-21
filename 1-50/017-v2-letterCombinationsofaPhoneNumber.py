class Solution:
    # 使用队列的解法，每次弹出一个字母
    def letterCombinations(self, digits: str) -> List[str]:
        from collections import deque
        d = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        lst = deque()
        res = []
        l = len(digits)
        if l == 0:
            return []
        # 先将第一个数字对应的字符放进去
        for i in d[digits[0]]:
            lst.append(i)
        while lst:
            # 每次弹出一个字符
            item = lst.popleft()
            # 当弹出的字符长度和数字长度相等时，表示弹出的字符生成完毕，加进列表中
            if len(item) == l:
                res.append(item)
            else:
                # 当弹出的字符长度和数字长度不等时，获取弹出字符的当前长度，进而拿到需要的下一位对应的数字，从而获得下一位的字母，将下一位字母加到弹出的字符后面，再压回队列即可
                for i in d[digits[len(item)]]:
                    lst.append(item+i)
                    # print(lst)
        return res
