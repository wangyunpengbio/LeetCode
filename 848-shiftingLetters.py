# Time Limited Exceed 初版
class Solution:
    # 单个字符的偏移
    def lettershift(self,letter:str,shift:int)->str:
        asiccRes = (ord(letter)-ord("a")+shift)%26+ord("a")
        return chr(asiccRes)
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        S = list(S)
        # 对于所有的shift，依次循环进行赋值。主要的超时在此处，可以一次计算好shift，然后只用进行一轮赋值
        for index,shift in enumerate(shifts):
            i = 0
            while i < index + 1:
                S[i] = self.lettershift(S[i],shifts[index])
                i = i + 1
        return "".join(S)