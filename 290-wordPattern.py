class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # 用字典把pattern和字符串统一成一种形式 键：当前字符串 值：从abcde开始的新id
        strWord = {}
        words = str.split(" ")
        i = ord("a") - 1
        for index in range(len(words)):
            if words[index] not in strWord:
                i = i + 1
                strWord[words[index]] = i
            words[index] = chr(strWord[words[index]])
        patternWord = {}
        patterns = list(pattern)
        i = ord("a") - 1
        for index in range(len(patterns)):
            if patterns[index] not in patternWord:
                i = i + 1
                patternWord[patterns[index]] = i
            patterns[index] = chr(patternWord[patterns[index]])
        return "".join(words) == "".join(patterns)
