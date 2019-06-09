class Solution:
    # 直接按空格拆分，然后从头往后找就可以了
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        wordlist = text.split(" ")
        for i in range(len(wordlist)-2):
            if wordlist[i] == first and  wordlist[i+1] == second:
                res.append(wordlist[i+2])
        return res