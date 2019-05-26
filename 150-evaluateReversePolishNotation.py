class Solution:
    # 使用栈即可
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while tokens:
            # print(stack,tokens)
            item = tokens.pop(0)
            if item in ["+", "-", "*", "/"]:
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(eval(num2 + item + num1)) # 整数除法只保留整数部分 使用int转换即可
                stack.append(str(res))
            else:
                stack.append(item)
        return int(stack[-1])