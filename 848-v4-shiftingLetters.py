class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        res = ""
        letter = 'abcdefghijklmnopqrstuvwxyz'
        # 倒着遍历，依次获得累加后的shift，暂存到sumtmp，直接使用
        for i in range(len(shifts)-1,-1,-1):
            if i!=len(shifts)-1:
                sumtmp = shifts[i] + sumtmp
            else:
                sumtmp = shifts[len(shifts)-1]
            res = res + letter[(letter.index(S[i])+sumtmp)%26]
        return res[::-1]