class Solution:
    def calculate(self, s: str) -> int:
        import re
        numbers = re.split("[+-/*]",s)
        operators = re.findall("[+-/*]",s)
        # 先把乘除符号前后的数字都计算完成
        i = 0
        while i < len(operators):
            if operators[i] == "*" or operators[i] == "/":
                op = operators.pop(i)
                num1 = numbers.pop(i)
                num2 = numbers.pop(i)
                if op == "*":
                    res = str(int(num1) * int(num2))
                else:
                    res = str(int(num1) // int(num2))
                numbers.insert(i,res)
                continue
            i = i + 1
        # 再计算加减
        result = int(numbers[0])
        for i in range(len(operators)):
            if operators[i] == "+":
                result = result + int(numbers[i+1])
            elif operators[i] == "-":
                result = result - int(numbers[i+1])
        return int(result)
