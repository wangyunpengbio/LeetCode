class Solution:
    def calculate(self, s: str) -> int:
        import re
        # 该函数用来计算没有括号的时候，算式的值
        def calculateNoBracket(s):
            s = s.replace("+-","-") # 字符串替换，因为数字虽然是非负整数，但是括号里面会算出来负数
            s = s.replace("--","+")
            numbers = re.split(r'[+-]',s)
            operaters = re.findall(r'[+-]',s)
            res = int(numbers[0])
            for i in range(len(operaters)):
                if operaters[i] == "+":
                    res = res + int(numbers[i+1])
                if operaters[i] == "-":
                    res = res - int(numbers[i+1])
            return str(res)
        # 使用栈结构，遇到括号先把括号里的值计算好
        stack = []
        for item in s:
            print(item)
            if item == " ":continue
            stack.append(item)
            if item == ")":
                stack.pop()
                insideBracket = ""
                while True:
                    item = stack.pop()
                    if item == "(":
                        res = calculateNoBracket(insideBracket)
                        stack.append(res)
                        break
                    insideBracket = item + insideBracket
        # 把剩下的值也算出来
        res = calculateNoBracket("0"+"".join(stack)) # 开头添0，是为了防止-5这样已经计算出来的话，重复计算有bug
        return int(res)
