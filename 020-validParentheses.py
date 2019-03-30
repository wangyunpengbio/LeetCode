class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈来解答
        stack = []
        mapping = {"}":"{",")":"(","]":"["}
        for char in s:
            if char in mapping:
                # 为了防止 "[])"此类字符串最后只剩")"pop会出错
                item = stack.pop() if stack else "#"
                if item != mapping[char]:
                    return False
            else:
                stack.append(char)
        if len(stack)==0:
            return True
        else:
            return False