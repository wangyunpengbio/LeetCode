# Time Limited Exceed 和v2相似的速度
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        letter = 'abcdefghijklmnopqrstuvwxyz'
        # 从第一个shift到倒数第二个shift；最后一个shift不用变
        for index in range(0,len(shifts)-1):
            for j in range(index+1,len(shifts)):
                shifts[index] = shifts[index] + shifts[j]
        res = ""
        for i,char in enumerate(S):
            res = res + letter[(letter.index(char)+shifts[i])%26]
        return res