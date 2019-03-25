class Solution:
    def romanToInt(self, s: str) -> int:
        # 受到整数转罗马数字启发，从后向前遍历，依次加起来就可以了
        valSet = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        result = 0
        i = 0
        while i < len(s):
            currentChar = len(s)-1-i
            if s[currentChar - 1: currentChar + 1] in valSet and currentChar - 1 >= 0:
                result = result - valSet[s[currentChar-1]] + valSet[s[currentChar]]
                i = i + 2
                continue
            if s[currentChar] in valSet:
                result = result + valSet[s[currentChar]]
                i = i + 1
        return result