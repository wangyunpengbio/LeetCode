# Time Limited Exceed 优化之后能通过更多一些的用例
class Solution:
    def lettershift(self,letter:str,shift:int)->str:
        asiccRes = (ord(letter)-ord("a")+shift)%26+ord("a")
        return chr(asiccRes)
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        # 从第一个shift到倒数第二个shift；最后一个shift不用变
        for index in range(0,len(shifts)-1):
            for j in range(index+1,len(shifts)):
                shifts[index] = shifts[index] + shifts[j]
        res = ""
        for i,char in enumerate(S):
            res = res + self.lettershift(char,shifts[i])
        return res